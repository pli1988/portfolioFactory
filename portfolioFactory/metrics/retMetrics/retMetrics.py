# -*- coding: utf-8 -*-
"""
Collection of return metrics to operate on pandas (time)series and dataframes

"""

import pandas as pd
import nympy as np


def main():
    pass

def averageHorizonReturn(data, horizon):
    
    ''' Calculate return over a horizon.

    Input: 
    Output:
    
    Example: averageHorizonReturn(data, horizon)
    
    '''
    
    returns = np.append([0], data.values)
    indexLevel = np.cumprod(1+returns)
    
    runningMax = np.maximum.accumulate(indexLevel)
    
    localDrawdown = indexLevel / runningMax -1
    
    return localDrawdown.min()
    
def annualizedSharpe(data, freq):
    
    '''Calculate sharpe ratio'''    
    
    pass

def cumulativeReturn(data, annualize):
    
    '''Calculate cumulative return'''
    
    pass


if __name__ == "__main__":
    main()
    
    
    
    