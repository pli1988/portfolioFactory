# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 22:09:49 2014

@author: peter
"""

import numpy as np
from . import customExceptions

# Move to utilities
def trimData(data):
    """ Function to drop leading and trailing NaN for timeseries
    
    trimData will return an error if there are NaN's in the middle of the series    
    
    Args:
        - data (Pandas time series): monthly timeseries
    
    Returns:
        Trimmed time series        
        
    """    
    
    # check if there are any NaN values in the middle
    if checkSeqentialMonthly(data.dropna().index):
        return data.dropna()
    else:
        raise customExceptions.badData('trimData')

def checkSeqentialMonthly(index):
    """ Function to check if dates for data timeseries are sequential
    
    Args:
        - data (Pandas time series): timeseries index
    
    Returns:
        True / False
        
    """    
    
    # Array of Months and Years
    months = index.month
    years = index.year
    
    # Difference in months % 12 -- this value should always be 1
    monthsDiff = np.mod(months[1:]-months[0:-1],12)
    
    # If months are sequential    
    if all(monthsDiff == 1):
        yearsDiff = years[1:] - years[0:-1]
        ix = np.where(yearsDiff == 1)
        
        # If years are sequential
        if all(months[ix] == 12):        
            return True        
        else:        
            return False        
    else:    
        return False
    

    