# -*- coding: utf-8 -*-
"""
Collection of risk metrics to operate on pandas series and dataframes

t
"""

import pandas as pd
import nympy as np


def main():
    pass


def maxDrawdown(data):
    
    
    returns = np.append([0], data.values)
    indexLevel = np.cumprod(1+returns)
    
    runningMax = np.maximum.accumulate(indexLevel)
    
    localDrawdown = indexLevel / runningMax -1
    
    return localDrawdown.min()
    
def annualizedVolatility(data):
    
    pass
    
def beta(X, y):
    
    pass


def VaR(data, horizon, confidence):
    
    pass

if __name__ == "__main__":
    main()
    
    
    
    