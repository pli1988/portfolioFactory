# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 17:15:47 2014

@author: Israel
"""
import pandas as pd
import numpy as np

def calcRollingReturns(df,window):
    ''' Function to calculate window-size rolling returns
    
        Note: assumes returns are in decimal form (ex. 0.02 represents 2%)
    
        Arguments:
        - df (dataframe) : returns matrix (tickers as columns)
        - window (int) : specifies size of rolling window
        
        Returns
        - pandas dataframe with rolling returns
    '''

    return (pd.rolling_apply(1+df,window=window,func=np.prod,min_periods=window) - 1)
      
