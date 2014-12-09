
"""

This module contains a collection of risk metrics to operate on pandas timeseries

Author: Peter Li
"""

import pandas as pd
import numpy as np
from ..utils import utils as utils

scalingFactor= {'d':  252, 'w': 52, 'm': 12, 'a': 1}

def main():
    pass

def maxDrawdown(data):
    """ Calculate maximum drawdown
    
    Args:
        data (Pandas timeseries): timeseries of returns
      
    Returns:
        Maximum peak to trough loss 
      
    """    
    
    cleanData = utils.trimData(data)
    
    # append zero to return series and compute level
    returns = np.append([0], cleanData.values)
    indexLevel = np.cumprod(1+returns)
    
    # Find running maximum
    runningMax = np.maximum.accumulate(indexLevel)
    
    # Percent change relative to running maximum
    localDrawdown = indexLevel / runningMax -1
    
    return localDrawdown.min()
    
def annualizedVolatility(data, freq):
    
    """ Calculate annalized volatility
    
    Args:
        data (Pandas timeseries): timeseries of returns
      
    Returns:
        Annualized volatility 
      
    """    
    
    cleanData = utils.trimData(data)         
    
    vol = np.std(cleanData)* np.sqrt(scalingFactor[freq])
    
    return vol
    
def VaR(data, horizon, probability):
    
    """ Calculate historical value at risk
    
     For a given return series, horizon, and probability (p), VaR is the threshold 
     loss value, such that the probability that the loss over the given time 
     horizon exceeds this value is p.[wikipedia] 
     
     historical VaR is calculated by taking the pth-quantile of the rolling returns 
     
     If the 95%, 1-Year VaR = -15%, then 95% of the time we would expect the 
     1-Year returns to be greater than -15%. 
    
    Example: VaR(data,12, 0.95)
    
    Args:
        - data (Pandas timeseries): timeseries of returns
        - horizon (num): number of periodss for historical VaR
        - confidence (num): confidence level 
      
    Returns:
        VaR
      
    """  
    
    cleanData = utils.trimData(data)

    # Calculate annualized rolling returns
    rollingReturns = pd.rolling_apply(cleanData, horizon, lambda x: np.prod(1 + x)**(12/horizon) - 1)
    
    VaR = np.percentile(rollingReturns.dropna(), 5)
    
    return VaR

## Move to utilities
#def trimData(data):
#    ''' Function to drop NaN at the beginning and end of a dataframe
#    
#    Function will return a data error is there are missing values in the middle    
#    
#    '''
#    # check if there are any NaN values in the middle
#    if checkSeqentialMonthly(data.dropna()):
#        
#        return data.dropna()
#        
#    else:
#        
#        raise badData('trimData')
#
#def checkSeqentialMonthly(data):
#    
#    months = data.index.month
#    years = data.index.year
#    
#    monthsDiff = np.mod(months[1:]-months[0:-1],12)
#    
#    if all(monthsDiff == 1):
#    
#        yearsDiff = years[1:] - years[0:-1]
#        ix = np.where(yearsDiff == 1)
#    
#        if all(months[ix] == 12):
#            
#            return True
#        else:
#            return False 
#    else:
#        return False

if __name__ == "__main__":
    main()
    

class badData(Exception):
    pass
    
    