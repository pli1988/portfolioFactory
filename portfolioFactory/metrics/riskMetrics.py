"""
riskMetrics is a module that contains a collection of functions to compute
common risk metrics on Pandas timeseries.

Author: Peter Li

"""

import pandas as pd
import numpy as np
from ..utils import utils as utils
from ..utils import customExceptions as customExceptions

def main():
    pass

def maxDrawdown(data):
    """  Function to calculate maximum drawdown
    
    Maximum drawdown is the maximum peak-to-trough loss    
    
    Input:
        data (Pandas timeseries): timeseries of returns
      
    Returns:
        drawdown (scalar): maximum % loss 
      
    """    
    
    cleanData = utils.processData(data)
    
    # append zero to return series and compute level
    returns = np.append([0], cleanData.values)
    indexLevel = np.cumprod(1+returns)
    
    # Find running maximum
    runningMax = np.maximum.accumulate(indexLevel)
    
    # Percent change relative to running maximum
    localDrawdown = indexLevel / runningMax -1
    
    return localDrawdown.min()
    
def annualizedVolatility(data):
    
    """ Function to calculate annalized volatility
    
    Input:
        data (Pandas timeseries): timeseries of returns
      
    Returns:
        Annualized volatility 
      
    """    
    
    cleanData = utils.processData(data)         
    
    vol = np.std(cleanData)* np.sqrt(12)
    
    return vol
    
def VaR(data, horizon, probability):
    """ Function to Calculate historical value at risk
    
     For a given return series, horizon, and probability (p), VaR is the threshold 
     loss value, such that the probability that the loss over the given time 
     horizon exceeds this value is p.[wikipedia] 
     
     historical VaR is calculated by taking the pth-quantile of the rolling returns 
     
     If the 95%, 1-Year VaR = -15%, then 95% of the time we would expect the 
     1-Year returns to be greater than -15%. 
    
    Example: VaR(data,12, 95)
    
    Input:
        - data (Pandas timeseries): timeseries of returns
        - horizon (num): number of periodss for historical VaR
        - confidence (num): confidence level in percent i.e.enter 95 for 95%
      
    Returns:
        VaR
      
    """  
    
    cleanData = utils.processData(data)
    
    if ((1<=horizon<=len(cleanData)) & isinstance(horizon, int)) & (0<=probability<=100):            
    
        # Calculate rolling returns
        rollingReturns = pd.rolling_apply(cleanData, horizon, lambda x: np.prod(1 + x) - 1)
        
        VaR = np.percentile(rollingReturns.dropna(), 100 - probability)
        
        return VaR
        
    else:
        
        raise customExceptions.invalidInput('VaR')

if __name__ == "__main__":
    main()   