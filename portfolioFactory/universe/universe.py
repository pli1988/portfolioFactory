
import pandas as pd
import numpy as np

class universe(object):
    ''' Universe is a class to represent the set of possible investments. 
    
    This class contains asset class returns and associated metadata.     
    
    Public Attributes:
        - parameters
        - assetReturns
        - summary
        - tickers
    '''
    
    def __init__(self,configPath):
        
        '''Reads in parameters from configPath and loads asset returns      
        
        Args:
            configPath (str): location of config file
          
        '''
        
        self.parameters = self.__setParameters(configPath) 
        self.__setReturn()
        
# TODO: Add checks for if file exists     
    def __setParameters(self, configPath):
        """ Method to read config file
        
        Note:
            configPath is assumed to be a .txt file with (at least) the following fields:
              - totallReturnFilePath
        
        Args:
            configPath (str): location of config file
          
        Returns:
            A dict with {key = parameter name: value = parameter value} 
          
        """
        
        # Load Data
        parameters = pd.read_table(configPath , sep = '=', index_col = 0, header = None)
        parameters.columns = ['values']        
        
        # Strip spaces
        parameters = parameters.astype('string')        
        parameters.index = parameters.index.map(str.strip)        
        parameters = parameters['values'].map(str.strip)
        
        return parameters.to_dict()
        
    def __setReturn(self):
        
        """ Method to set self.returns
        
        Note:
            Assumes returns data exists in a pickled  pandas data frame
                    
        """
        
        totalReturnsPath = self.parameters['totalReturnFilePath']
               
        self.assetReturns = pd.read_pickle(totalReturnsPath)
        
    def __setTickers(self):
        
        """ Method to set self.tickers

        Extracts asset class tickers from returns dataframe
        
        """        
        
        self.tickers = self.returns.columns.values

# Maybe move to utility ???
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