# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 16:05:31 2014

@author: peter
"""
# Example
testUniverse = universe('usEquityConfig.txt')

# TODO: Add frequency parameter ??? maybe
# TODO: Add Checks
# TODO: Move fetchPrices to utility
# TODO: Add summary 

import pandas as pd
import pandas.io.data as web

class universe(object):
    '''
    Class to represent investment universe. This class contains most of the 'data'
    Input is read in from a config file. 
    
    Attributes:
        - parameters
        - returns
        - summary *
    Methods:
        - __readConfig
        - __setReturn
        - __getTickers
    '''
    def __init__(self,configPath):
        
        self.parameters = self.__readConfig(configPath) 
        self.__setReturn()
        
    def getTickers(self):
            
        tickerPath = self.parameters['tickerPath']
                
        with open(tickerPath, 'r') as f:
            tickers = f.read()
                   
        tickers = tickers.strip().split(',')
        tickers = map(str.strip,tickers)
               
        return tickers
        
    def __readConfig(self, configPath):
    
        parameters = pd.read_table(configPath , sep = '=', index_col = 0, header = None)
        parameters.columns = ['values']        
        
        parameters = parameters.astype('string')        
        parameters.index = parameters.index.map(str.strip)        
        parameters = parameters['values'].map(str.strip)
        
        return parameters.to_dict()
        
    def __setReturn(self):
        
        names = self.getTickers()
        returnsPanel = {n: universe.fetchPrices(n, self.parameters['startDate'], self.parameters['endDate']) for n in names}        
        
        px = pd.DataFrame(returnsPanel)
        px = px.asfreq('B').fillna(method = 'pad')
        rets = px.pct_change()
        
        self.returns = rets
          
    @staticmethod
        
    def fetchPrices(ticker, start, end):
    
        return web.get_data_yahoo(ticker, start, end)['Adj Close']
        



