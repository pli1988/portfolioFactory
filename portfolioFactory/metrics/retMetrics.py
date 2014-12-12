"""
retMetrics is a module that contains a collection of functions to compute
return metrics on Pandas timeseries.

Author: Peter Li

"""

import pandas as pd
import numpy as np
from ..utils import utils as utils
from ..utils import customExceptions as customExceptions

def main():
    pass

def averageHorizonReturn(data, horizon):
    
    ''' Function to calculate average returns over a horizon.
    
    averageHorizonReturn computes the average of rolling horizon returns
    
    Example: average 1-Year return
    
        >> averageHorizonReturn(data, 12)

    Input: 
        - data (timeseries): timeseris of monthly retun data
        - horizon (int): window size for rolling analysis
        
    Returns:
        - averageRollingReturn (scalar)
       
    '''
    
    cleanData = utils.processData(data) 
    
    if (1 <= horizon <= len(cleanData)) & isinstance(horizon, int):    
    
        return np.mean(rollingReturn(cleanData, horizon))
        
    else:
        
        raise customExceptions.invalidInput('averageHorizonReturn') 
        
    
def cumulativeReturn(data):
    
    ''' Function to calculate cumulative returns.
    
    Input: 
        - data (timeseries): timeseris of monthly retun data
        
    Returns:
        - cumulative return (scalar)
       
    '''
    
    cleanData = utils.processData(data)    
    
    return np.prod(1 + cleanData) - 1    

def rollingReturn(data, horizon):
    ''' Function to calculate rolling returns over a horizon.
    
    rollingReturn computes the returns over a horizon
    
    Example: average 1-Year return
    
        >> averageHorizonReturn(data, 12)

    Input: 
        - data (timeseries): timeseris of monthly retun data
        - horizon (int): window size for rolling analysis
        
    Returns:
        - rollingReturn (timeseries): timeseries of the same size as data
       
    '''
    
    cleanData = utils.processData(data)
    
    if (1 <= horizon <= len(cleanData)) & isinstance(horizon, int):    

        # Calculate rolling returns
        rollingReturns = pd.rolling_apply(cleanData, horizon, lambda x: np.prod(1 + x) - 1)        
        
        return rollingReturns
        
    else:
        
        raise customExceptions.invalidInput('averageHorizonReturn') 
        
if __name__ == "__main__":
    main()    
    