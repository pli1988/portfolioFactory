"""
The universe module contains the universe class. 

Author: Peter Li

"""
import pandas as pd
import numpy as np

from ..utils import utils as utils
from ..utils import customExceptions

class universe(object):
    ''' Universe is a class to represent the set of possible investments. 
    
    This class contains asset class returns and associated metadata.     
    
    Public Attributes:
        - assetReturns
        - summary
        - filePath
        - tickers
    '''

    def __init__(self, name, assetReturnsPath):
        
        '''Pass name and select location of asset return file
        
        Note: assetReturnsPath sholud be the location of a pickled dataframe        
        
        Args:
            name (str): universe name
            assetReturnPath(str): location of assetReturns
          
        '''

        self.filePath = assetReturnsPath
        
        if isinstance(name, str):
            self.name = name
        else:
            raise customExceptions.badData('Name must be a str')
        
        try:
            self.__setReturn()
            self.__setTickers()
        except:
            raise 

    def __setReturn(self):
        
        """ Method to set self.assetReturns
        
        setReturns attempts to load the file in self.filePath and set it as
        self.assetReturns. The methods checks the validity of the file and returns
        an error if checkData fails.         
        
        Note:
            Assumes returns data exists in a pickled Pandas data frame
                    
        """
        
        # Trys to read data file
        try:    
            data = pd.read_pickle(self.filePath)
            
            # Checks if read file meets criteria
            if self.checkData(data):
                
                self.assetReturns = data
                
            else:
                
                raise customExceptions.badData('Pickled file is not a proper Dataframe')
                
        except:
            
            raise customExceptions.badData('File is not a pickle')
        
    def __setTickers(self):
        
        """ Method to set self.tickers

        Method to extracts asset class tickers from returns dataframe
        
        """        
        
        self.tickers = self.assetReturns.columns.values

    def computeSummary(self):
        """ Method to compute summary statistics for return dataframe
        
        Returns:
            Data frame containing:
                - count data
                - count missing values
                - min
                - max
                - standard deviation (unadjusted)        
                
        """
        
        df = self.assetReturns
        
        # Summary statistiscs
        summary = df.describe()
        
        # Number of NaNs
        missingCounts = np.sum(df.apply(pd.isnull,0))
        
        # Format output dataframe
        out = summary.ix[['count', 'mean', 'max', 'min', 'std']].T
        out['missing'] = missingCounts
    
        outOrder = ['count', 'missing', 'mean', 'max', 'min', 'std']
        
        self.summary = out[outOrder]
        
        return self.summary
        
    def checkData(self, data):     
        """ Method to check data validity for return dataframe
        
        checkData will check if the returns data is a pandas dataframe of 
        sequential monthly data.
        
        Returns: True/False
 
     """           
        
        # Check if returns is a Dataframe
        if isinstance(data, pd.DataFrame):
        
            # Check if index is dates
            if isinstance(data.index, pd.tseries.index.DatetimeIndex):
        
                # Check if sequential
                if utils.checkSeqentialMonthly(data.index):
                    
                    return True

        return False
                    