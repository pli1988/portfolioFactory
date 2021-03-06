# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import datetime
import portfolioFactory
from ..strategy import strategy as strategy
from ..utils.customExceptions import *

class portfolio(object):
    
    ''' Porfolio is a class to represent investment porfolios. 
    
    This class contains returns generated by the portfolio and associated metadata.
    
    A portfolio is composed of a linear combination of strategies 
    
    Public Attributes:
        - returns (df): a single-column dataframe representing the porfolio returns
        - strategies (list) : a list with the strategy names composing the portfolio
        - weights (list) : a list containing the weighting of each strategy

    '''
    
    def __init__(self,strategyPool,weights):
        ''' Method to intialize a porfolio object
            
        Args:
            strategyPool (list): a list of strategy objects
            universe (universe): a list of numeric strategy weights
        '''
        
        # confirm both inputs are lists
        if type(strategyPool)!=list or type(weights)!=list:
            raise notListError
        
        # confirm lists are the same length
        if len(strategyPool)!=len(weights):
            raise listMismatch
        
        # confirm elements of strategyPool are strategy objects
        for s in strategyPool:
            if isinstance(s,portfolioFactory.strategy.strategy.strategy)==False:
                raise notStrategyError
    
        # confirm elements of weights are numeric
        for w in weights:
            if isinstance(w,(int, long, float))==False:
                raise badWeightError
        
        
        self.strategies = [x.parameters['name'] for x in strategyPool]
        self.weights = weights[:]
        

        portWeights = pd.DataFrame(pd.Series(self.weights, index=self.strategies))
        portElements = {x.parameters['name'] : x.strategyReturns for x in strategyPool}
        portData = pd.DataFrame(portElements)
        
        portReturns =  portData.dot(portWeights)
        portReturns.columns = ['portReturns']
        self.portReturns = portReturns

      