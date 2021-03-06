# -*- coding: utf-8 -*-
"""
Created on Sat Dec 06 15:27:38 2014

@author: Israel
"""


# TODO: Add Checks
# TODO: Add summary
# TODO: handle if first window data is missing

import pandas as pd
import numpy as np
import datetime
import portfolioFactory
from ..utils.customExceptions import *
from ..utils.utils import setParameters


class strategy(object):

    ''' Strategy is a class to represent investment strategies. 
    
    This class contains returns generated by the strategy and associated metadata.
    
    A strategy is defined by:
        - the investment universe on which the strategy is defined
        - the signal used to select specific investments
        - the weighting scheme used to allocate funds across the selected investments
        - these 3 components are used to generate the value of that
    
    Public Attributes:
        Data attributes:
        - signal: dataframe containing the signal used to select stocks (example: rolling returns)
        - selection: dataframe of zeros and ones to identify the selected investments
        - weights: dataframe containing the weights allocated to each selected investment
        - strategy: dataframe with the value of each investment and the total value ('value')
        - parameters: dictionary containing metadata
        
        Parameters Dictionary:
        - universe: the name of universe object on which the strategy is defined
        - signalPath: path to pickled dataframe with signal data
        - rule: the cutoff point for selecting investments
        - window: size of window between rebalancing 

    '''
    
    
    
    def __init__(self,universe,configPath):
        ''' Method to intialize a strategy object
        
            1) Reads in parameters from configPath      
            2) Sets signal as attribute
            3) Selects investments based on signal and sets as attribute
            4) Calculates weights ands sets as attribute
            5) Calculates strategy values and sets as attribute
            
        Args:
            configPath (str): location of config file
            universe (universe): universe on which the strategy is defined 
          
        '''
        
        # pull parameters from config file
        self.parameters = setParameters(configPath)
        self.parameters['universe']=universe.name
        
        
        # verify input
        self.__verifyUserInput(universe)
        
        # pull signal data
        self.__setSignal()
        
        # check date overlap between returns and signal data
        self.__checkOverlap() 
        
        # set attributes 
        self.__setSelection()
        self.__setWeights()
        self.__setStrategy()
        

        
    def setParameters(configPath):
        """ Method to read config file
        
        Note:
            configPath is assumed to be a .txt file with (at least) the following fields:
              - name : a name/description for the strategy
              - signalPath: signal data location 
              - rule: the cutoff point for selecting investment (positive/negative int-->pick top/bottom S investments)
              - window: time-span between rebalancing

        
        Args:
            configPath (str): location of config file
          
        Returns:
            A dict with {key = parameter name: value = parameter value} 
            
        """
        
        # Load Parameters Data
        try:
            parameters = pd.read_table(configPath , sep = '=', index_col = 0, header = None)
        except IOError:
            raise InvalidParameterPath(configPath)
            
        parameters.columns = ['values']        
        
        # Strip spaces
        parameters = parameters.astype('string')        
        parameters.index = parameters.index.map(str.strip)        
        parameters = parameters['values'].map(str.strip)
        
        return parameters.to_dict()
          

    def __verifyUserInput(self,universe):
        
        
        # 1) make sure that passed universe is a universe object
        if isinstance(universe,portfolioFactory.universe.universe.universe)==False:
            raise notUniverseObject
        else:
            self._fullReturns = universe.assetReturns.copy()
            
        # 2) make sure config file has necessary inputs
        expectedInputs = ['name','signalPath', 'rule','rebalanceWindow','universe']
        
        for inp in expectedInputs:
            if str(inp) not in self.parameters.keys():
                raise missingInput(inp) 
                
        for inp in self.parameters.keys():
            if str(inp) not in expectedInputs:
                raise unexpectedInput(inp)
                
        # 3) ensure window is numeric
        try:
            self._window = int(self.parameters['rebalanceWindow'])
        except ValueError:
            raise windowNotInt()
            
        if self._window<1:
            raise windowNegative(self._window)
            
        # 3) ensure rule is numeric
        try:
            self._rule = int(self.parameters['rule'])
        except ValueError:
            raise ruleNotInt(self.parameters['rule'])
            

        
        
    def __setSignal(self):
        """ Method to set self.signal
        
            Note: signal data must be a pickled pandas dataframe
        
        """
        try:  
            self._fullSignal = pd.read_pickle(self.parameters['signalPath'])
        except IOError:
            raise invalidSignalPath(self.parameters['signalPath'])
            
    
        
    def __checkOverlap(self):
        """ Method to extract overlap between signal and assetReturns data
        
            Note: Method also ensures that there is sufficient overlap in terms of tickers and dates
        """
        
        # obtain dates of overlap (ensure intersection exists)
        beginOverlap = (self._fullSignal.index).intersection(self._fullReturns.index).min()
        endOverlap = (self._fullSignal.index).intersection(self._fullReturns.index).max()
        if isinstance(beginOverlap,pd.tslib.NaTType) or isinstance(beginOverlap,pd.tslib.NaTType):
            raise noTimeOverlap
        
        # obtain overlapping ticker  (ensure intersection exists)
        tickerOverlap = list(set(self._fullSignal.columns).intersection(set(self._fullReturns.columns)))
        if len(tickerOverlap)==0:
            raise noTickerOverlap
        
        self._tickers = tickerOverlap
        self._returns = self._fullReturns.ix[beginOverlap:endOverlap][self._tickers]
        self._rebalanceDates = self._returns.index[::self._window]
        self.signal = self._fullSignal.ix[self._rebalanceDates][self._tickers]
                
 


      
    def __setSelection(self):
        """ Method to set self.selection
        
            Note: includes checks to make sure there are enough non-Nan observations to make full selection
        
        """
        
        # Case 1: cutoff rule is positive
        if self._rule > 0:
            mask = self.signal.rank(axis=1)<=(self._rule)*(self.signal.notnull())
        # Case 2: cutoff rule is negative    
        if self._rule < 0:
            mask = (-1*self.signal).rank(axis=1)<=(self._rule)*(self.signal.notnull())
        
        # Check to make sure there are enough non-Nan values
        diff = np.abs(self._rule)*mask.shape[0] - mask.sum(axis=1).sum()
        if diff > 0:
            raise notEnoughSignals(diff)
            
        self.selection = 1*mask
            
         
         
         
            
    def __setWeights(self):
        """ Method to set self.weights
        
        
            Note: normalizes so that the weights for each day sum to 1
        
        """
        
        rawWeights = pd.DataFrame(1,index=self._rebalanceDates,columns=self._tickers)*self.selection
        sumWeights = rawWeights.sum(axis=1).replace(0,1)
        normWeights = rawWeights/sumWeights
        self.weights = normWeights
        
        
        
        
    def __setStrategy(self):
        """ Method to set self.strategy
        
            Calculates the value of each investment and the overall value of the strategy,
            using the weights based on the input parameters.
        
            Returns:
                A dataframe with the value of each investment and and the overall strategy ('value') 
        """
        
        # set parameters and lists to prepare for merge        
        weights = self.weights.copy()
        weightTickers = [str(x)+'_w' for x in weights.columns]
        weights['rebalance'] = 1
         
        # merge the returns dataframe with the weights dataframe and forward fill weight data
        merged = pd.merge(self._returns,weights,how='left',left_index=True,right_index=True,suffixes=['_r','_w'])
        merged['block'] = None
        merged.loc[merged.rebalance==1,['block']] = np.arange((merged.rebalance==1).sum())
        merged['block'] = merged['block'].fillna(method='ffill')
        merged = merged.drop('rebalance',axis=1)
        merged[weightTickers] = merged[weightTickers].fillna(method='ffill')
         
        # before grouping by block (time span between rebalancing), set a global to 0.
        # this global is used to carry infomation (value on previous day) across the groups/blocks.
        global portValueGlobal
        portValueGlobal=0
        rebalanced = merged.groupby('block').apply(strategy.calcRebalancing,tickers=self._tickers)
         
        # keep the values of interest and calculate returns
        columnsToKeep = self._tickers[:]
        columnsToKeep.extend(['block','value'])
        self.values = rebalanced[columnsToKeep]
        strategyReturns = (self.values).pct_change()['value']
        strategyReturns.iloc[0]= (self.values.value[0])-1
        self.strategyReturns = strategyReturns




    @ staticmethod
    # will be moved to util
    def calcRebalancing(df,tickers):
        global portValueGlobal
        
        for t in tickers: 
            df[t] = ((1+df[t+'_r']).cumprod())*(df[t+'_w'])*portValueGlobal
        df['value'] = df[tickers].sum(axis=1)
        
        # chunk of code below where the global tracking is if/elsed is
        # due to a bug in pandas groupby. See warning at url below.
        # http://pandas.pydata.org/pandas-docs/dev/groupby.html
        
        if portValueGlobal==0:
            portValueGlobal=1
        else:
            portValueGlobal = df['value'].iloc[-1]
        #print df
        return df



        