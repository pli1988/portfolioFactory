# -*- coding: utf-8 -*-
"""
Collection of return metrics to operate on Pandas timeseries

Author: Peter Li
"""

import pandas as pd
import numpy as np
from ..utils import utils as utils
from ..utils import customExceptions as customExceptions



def main():
    pass

def averageHorizonReturn(data, horizon):
    
    ''' Calculate return over a horizon.

    Input: 
    Output:
    
    Example: averageHorizonReturn(data, horizon)
    
    '''
    
    cleanData = utils.processData(data) 
    
    if 1<=horizon<=len(cleanData):    
    
        return np.mean(rollingReturn(cleanData, horizon))
    else:
        raise customExceptions.invalidInput('averageHorizonReturn') 
        
    
def cumulativeReturn(data):
    
    '''Calculate cumulative return'''
    
    cleanData = utils.processData(data)    
    
    return np.prod(1 + cleanData) - 1    

def rollingReturn(data, horizon):
    
    cleanData = utils.processData(data)
    
    if 1<=horizon<=len(cleanData):    

        # Calculate rolling returns
        rollingReturns = pd.rolling_apply(cleanData, horizon, lambda x: np.prod(1 + x) - 1)        
        return rollingReturns
        
    else:
        raise customExceptions.invalidInput('averageHorizonReturn') 
        
if __name__ == "__main__":
    main()    