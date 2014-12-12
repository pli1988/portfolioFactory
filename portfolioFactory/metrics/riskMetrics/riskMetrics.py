# -*- coding: utf-8 -*-
"""
Collection of risk metrics to operate on pandas (time)series and dataframes

"""

import pandas as pd
import numpy as np


def main():
    pass

def maxDrawdown(data):
    
    ''' Calculate Maximum Drawdown.

    Input: time series of price levels (first to last)
    Output: Maximum peak to trough performance
    
    '''
    
    returns = np.append([0], data.values)
    indexLevel = np.cumprod(1+returns)
    
    runningMax = np.maximum.accumulate(indexLevel)
    
    localDrawdown = indexLevel / runningMax -1
    
    return localDrawdown.min()
    
def annualizedVolatility(data, freq):
    
    
    ''' Calculate Annualized Volatility.

    Input: time series of returns, frequenc of data
    
    Output: Annualized Volatility 
    
    '''    
    
    scalingFactor= {'d':  252, 'w': 52, 'm': 12, 'a': 1}    
    
    vol = np.std(data)* np.sqrt(scalingFactor[freq])
    
    return vol
    
def beta(X, y):
    
    pass


def VaR(data, frequency, horizon, confidence):
    
    pass

if __name__ == "__main__":
    main()
    
    
    
    