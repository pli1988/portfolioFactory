

"""
test_portfolio is a module to run unit tests for portfolio Class


To run all test:  >> python -m unittest discover

Author: Israel Malkin
"""

import unittest
import pandas as pd

import portfolioFactory.universe.universe as universe
import portfolioFactory.strategy.strategy as strategy
import portfolioFactory.portfolio.portfolio as portfolio
from ..utils import customExceptions as customExceptions


class TestPortfolioFunctions(unittest.TestCase):

    def createUniverse(self,config):
        
        location = "./portfolioFactory/strategy/SampleFiles/"
        return universe.universe('name',location+config)
        
        
    def createStrategy(self,universe,config):
        
        location = "./portfolioFactory/strategy/SampleFiles/"        
        return strategy.strategy(universe,location+'strategyConfig_'+config+'.txt')
        
    def createPortfolio(self,a,b):
        
        location = "./portfolioFactory/strategy/SampleFiles/"        
        return portfolio.portfolio(a,b)
        
        

        
##############################################################################
# Test bad inputs
##############################################################################
        
    def testBadInput_NotList(self):
        # input must be in list format
        a = 55
        b = 77
        self.assertRaises(customExceptions.notListError,self.createPortfolio,a,b)
        
        
    def testBadInput_LengthMatch(self):
        # length of inputs must match
        a = [55]
        b = [77,'aa']
        self.assertRaises(customExceptions.listMismatchError,self.createPortfolio,a,b)
        
        
        
    def testBadInput_TypeIssue(self):
        # the types in strategyPool must all be strategy objects
        a = [55,55]
        b = [77,'aa']
        self.assertRaises(customExceptions.notStrategyError,self.createPortfolio,a,b)
        
        
    def testBadInput_BadWeight(self):
        # weights must numeric
        configUni = 'uni_early'
        configStr = '1_5'
        testUni = self.createUniverse(configUni)
        testStr = self.createStrategy(testUni,configStr)
        
        a = [testStr,testStr]
        b = [77,'aa']
        self.assertRaises(customExceptions.badWeightError,self.createPortfolio,a,b)
         
        

        


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSPortfolioFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)
        
