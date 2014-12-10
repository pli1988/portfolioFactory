
"""

This module contains a collection of risk metrics to operate on pandas timeseries

Author: Peter Li
"""

import pandas as pd
import numpy as np
from ..utils import utils as utils

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
    
def annualizedVolatility(data):
    
    """ Calculate annalized volatility
    
    Args:
        data (Pandas timeseries): timeseries of returns
      
    Returns:
        Annualized volatility 
      
    """    
    
    cleanData = utils.trimData(data)         
    
    vol = np.std(cleanData)* np.sqrt(12)
    
    return vol
    
def VaR(data, horizon, probability):
# TODO: Checks for invalide probability and horizon
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
    
    VaR = np.percentile(rollingReturns.dropna(), 1 - probability)
    
    return VaR

if __name__ == "__main__":
    main()   