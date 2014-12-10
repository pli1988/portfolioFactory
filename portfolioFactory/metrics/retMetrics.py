# -*- coding: utf-8 -*-
"""
Collection of return metrics to operate on pandas (time)series and dataframes

Author: Peter Li
"""

import pandas as pd
import numpy as np
from ..utils import utils as utils


def main():
    pass

def averageHorizonReturn(data, horizon):
    
    ''' Calculate return over a horizon.

    Input: 
    Output:
    
    Example: averageHorizonReturn(data, horizon)
    
    '''
    return np.mean(rollingReturn(data, horizon))
    
def cumulativeReturn(data):
    
    '''Calculate cumulative return'''
    
    cleanData = utils.trimData(data)    
    
    return np.prod(1 + cleanData) - 1    

def rollingReturn(data, horizon):
    
    cleanData = utils.trimData(data)

    # Calculate rolling returns
    rollingReturns = pd.rolling_apply(cleanData, horizon, lambda x: np.prod(1 + x) - 1)
    
    return rollingReturns

if __name__ == "__main__":
    main()
    
    
    
    