# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 22:30:17 2014

@author: Israel
"""
import pandas as pd
from ..exceptions.exceptions import *

def setParameters(configPath):
        """ Function to read config file
        
        Note:
            configPath is assumed to be a .txt file with (at least) the following fields:
              - name : a name/description for the strategy
              - signalPath: signal data location 
              - rule: the cutoff point for selecting investment (positive/negative int-->pick top/bottom S investments)
              - window: time-span between rebalancing

        
        Args:
            configPath (str): location of config file
          
        Returns:
            A dict with {key = parameter name: value = parameter value} 
            
        """
        
        # Load Parameters Data
        try:
            parameters = pd.read_table(configPath , sep = '=', index_col = 0, header = None)
        except IOError:
            raise InvalidParameterPath(configPath)
            
        parameters.columns = ['values']        
        
        # Strip spaces
        parameters = parameters.astype('string')        
        parameters.index = parameters.index.map(str.strip)        
        parameters = parameters['values'].map(str.strip)
        
        return parameters.to_dict()