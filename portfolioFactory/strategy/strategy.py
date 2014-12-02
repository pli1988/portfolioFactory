# -*- coding: utf-8 -*-

# Example
# testStrategy = strategy(testUniverse,'usEquityConfig_strategy.txt')



# TODO: Add Checks
# TODO: Add MarketCap capabilities
# TODO: Add summary 
# TODO: Add more schemes and weighting functions
# TODO: Check with Peter about weighting baseline
# TODO: Check with Peter about fetching universe (is it ok?)
# TODO: Initial weights on momentum 
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
        - weights
        - summary *
    Methods:
        - __readConfig
        - __setWeights
        - __getTickers
    '''
    def __init__(self,returnsUniverse,configPath):
        
        self.parameters = self.__readConfig(configPath)
        self.universe = returnsUniverse.returns
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
        
        
    def __setWeights(self):
        
        weightTickers = self.getTickers()
        weightDates = pd.date_range(self.parameters['startDate'],self.parameters['endDate'], freq=self.parameters['frequency']+'B')
        weightUniverse = self.universe
        weightFrequency = self.parameters['frequency']

        
        if self.parameters['strategySignal']=='equal':
            self.weights = strategy.__fillWeights_equal(weightTickers,weightDates)
        
        if self.parameters['strategySignal']=='momentum':
            functionMap = {'linear': strategy.__linearWeight,'squared': strategy.__squaredWeight,'rank': strategy.__rankCut, 'none': None}
            momentumSpec = [ self.parameters['cutoff'], functionMap[self.parameters['scheme']], functionMap[self.parameters['weight']] ]
            # momentumSpec = [cutoff value, scheme function, weight function]
            self.weights = strategy.__fillWeights_momentum(weightUniverse,weightTickers,weightDates,weightFrequency,momentumSpec)



    @ staticmethod
    
    def __fillWeights_equal(tickers,dates):
        return pd.DataFrame(1/len(tickers),columns=tickers,index=dates)
    
    
    @ staticmethod
    
    def __fillWeights_momentum(universe,tickers,dates,freq,spec):
        cumReturns = strategy.__calcCumReturns(universe,tickers,dates,freq)
        return cumReturns.apply(strategy.__selectMomentum,axis=1,spec=spec)

        
    @ staticmethod
    
    def __calcCumReturns(universe,tickers,dates,freq):
        return (pd.rolling_apply(1+universe[tickers],window=int(freq),func=np.prod) - 1).ix[dates]
    
    @ staticmethod
    
    def __selectMomentum(data,spec):
        # momentumSpec = [cutoff value, scheme function, weight function]
        sorted = data.sort(inplace=False)
        maskUpper,maskLower = spec[1](data,sorted,spec[0])
        weight = spec[2](data)
        unscaled =  ((1*maskUpper)-(1*maskLower))*weight
        scaled = unscaled/unscaled.sum(axis=1)
        return scaled
        
    @ staticmethod
    
    def __rankCut(data,sorted,bound):
        upper = (data>=sorted[-1*int(bound)])
        lower = (data<=sorted[int(bound)-1])
        return upper,lower
        
    @ staticmethod
    
    def __linearWeight(data):
        return np.absolute(data)
        
    @ staticmethod
    
    def __squaredWeight(data):
        return data*data





