# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 12:53:26 2014

@author: Israel
"""
import numpy as np
import pandas as pd
from . import customExceptions

def setParameters(configPath):
        """ Function to read config file
        
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
            raise customExceptions.invalidParameterPath(configPath)
            
        parameters.columns = ['values']        
        
        # Strip spaces
        parameters = parameters.astype('string')        
        parameters.index = parameters.index.map(str.strip)        
        parameters = parameters['values'].map(str.strip)
        
        return parameters.to_dict()
        
        
        
def calcRollingReturns(df,window):
    ''' Function to calculate window-size rolling returns
    
        Note: assumes returns are in decimal form (ex. 0.02 represents 2%)
    
        Arguments:
        - df (dataframe) : returns matrix (tickers as columns)
        - window (int) : specifies size of rolling window
        
        Returns
        - pandas dataframe with rolling returns
    '''
    #ensure parameters are specified correctly
    if type(df)!=pd.DataFrame:
        raise customExceptions.notDFError
    
    if type(window)!=int:
        raise customExceptions.windowNotInt
    
    if window<1:
        raise customExceptions.windowNegative
    
        
    return (pd.rolling_apply(1+df,window=window,func=np.prod,min_periods=window) - 1)
      
