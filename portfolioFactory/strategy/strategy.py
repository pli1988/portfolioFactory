# -*- coding: utf-8 -*-

# Example
testStrategy = strategy(testUniverse,'usEquityConfig_strategy.txt')



# TODO: Add Checks
# TODO: Add summary  
# TODO: Nan handling 

import pandas as pd
import pandas.io.data as web
import numpy as np
import math


class strategy(object):
    '''
    Class to represent strategy (security weights)
    Input is read in from a config file. 
    
    Attributes:
        - parameters
        - universe
        - signal
        - weights
        - summary *
    Methods:
        - __readConfig
        - __setWeights
        - __getTickers
        - __setSignal
        - __setWeights
    '''
    def __init__(self,returnsUniverse,configPath):
        
        self.parameters = self.__readConfig(configPath)
        self.universe = returnsUniverse.returns.copy()
        self.__setSignal()
        self.__setSelection()
        self.__setWeights()
        
        
        
    def __readConfig(self, configPath):
    
        parameters = pd.read_table(configPath , sep = '=', index_col = 0, header = None)
        parameters.columns = ['values']        
        
        parameters = parameters.astype('string')  
        parameters.index = parameters.index.map(str.strip)        
        parameters = parameters['values'].map(str.strip)
        
        return parameters.to_dict()
        

    def getTickers(self):
            
        tickerPath = self.parameters['tickerPath']
                
        with open(tickerPath, 'r') as f:
            tickers = f.read()
                   
        tickers = tickers.strip().split(',')
        tickers = map(str.strip,tickers)
               
        return tickers
        
        
    def __setSignal(self):
        
        signalTickers = self.getTickers()
        signalWindow = self.parameters['window']
        signalDates = pd.date_range(self.parameters['startDate'],self.parameters['endDate'], freq=self.parameters['window']+self.parameters['frequency'])
        signalUniverse = self.universe
        signalFrequency = self.parameters['frequency']
        
        if self.parameters['strategySignal']=='rollingReturns':
            self.signal = strategy.calcRollReturns(signalUniverse,signalWindow).ix[signalDates][signalTickers]


    def __setSelection(self):
        
        selectionCutoff = int(self.parameters['strategyRule'])
        
        self.selection = self.signal.apply(strategy.selectExtremes,C=selectionCutoff,axis=1)
            
            

    def __setWeights(self):
        
        weightTickers = self.getTickers()
        weightDates = pd.date_range(self.parameters['startDate'],self.parameters['endDate'], freq=self.parameters['window']+self.parameters['frequency'])
        weightFrequency = self.parameters['frequency']
        
        if self.parameters['strategyWeights']=='equal':
            weightData = pd.DataFrame(1,index=weightDates,columns=weightTickers)
            
        if self.parameters['strategyWeights']=='marketCap':
            weightData = strategy.getMarketCap(weightTickers,weightDates)
            
        if self.parameters['strategyWeights']=='custom':
            weightData = strategy.getCustomData()
        
        #filter weightdata through the selected equties
        upperRaw = weightData*(self.selection==1).astype(int)
        lowerRaw = weightData*(self.selection==-1).astype(int)
        #normalize so that the weights in each group sum to 1
        upperNormalized = upperRaw/upperRaw.sum(axis=1)
        lowerNormalized = lowerRaw/lowerRaw.sum(axis=1)
        #set weights
        self.weights = upperNormalized - lowerNormalized


     

    @ staticmethod       
    def getMarketCap(tickers,dates):
        ''' Returns dataframe with market capitalization data for the specified tickers & dates
            Data is from Quandl with quarterly frequency.'''  
        
        # load market cap data from CSV and prep for merging
        mc = pd.read_csv('MarketCap/marketCap_clean.csv') 
        mc = mc[mc['tic'].isin(tickers)]
        mc = mc.set_index(['year','quarter','tic'])
        mc = mc.unstack(level=2)
        mc.columns = mc.columns.droplevel(0)
        mc = mc.reset_index()

        # Intialize an empty dataframe with index set to dates of interest and columns=['year','quarter'] 
        emptyDates = pd.DataFrame(index=dates)
        emptyDates['year'],emptyDates['quarter'] = emptyDates.index.year, emptyDates.index.quarter

        
        # Merge the quarterly-frequency market cap data to the empty dates frame to obtain data proper frequency
        marketCap = emptyDates.reset_index().merge(mc, how="left", on=['year','quarter']).set_index('index')
        marketCap.drop(['year','quarter'],axis=1,inplace=True)
        return marketCap

        
    @ staticmethod
    # will be moved to util
    def calcRollReturns(returns,spansize):
        ''' Returns spansize-window rolling returns for the specified dates and tickers from universe.
            Assumes returns are in decimal form (ex. 0.02 is a 2% return)''' 
        
        return (pd.rolling_apply(1+returns,window=int(spansize),func=np.prod) - 1)

    
    @ staticmethod
    # will be moved to util
    def selectExtremes(series,C):
        '''Returns a transformed series with: 
           - The C largest elements in the passed series filled with 1
           - The C smallest elements in the passed series filled with -1 
           - All other elements filled with 0                      '''
        print     
        sorted = series.sort(inplace=False)
        maskUpper = (series>=sorted[-1*C])
        maskLower = (series<=sorted[C-1])
        return (1*maskUpper)+(-1*maskLower)
        
    


        






