

"""
test_strategy is a module to run unit tests for strategy Class


To run all test:  >> python -m unittest discover

Author: Israel Malkin
"""


import unittest
import pandas as pd
import numpy as np

import portfolioFactory.universe.universe as universe
import portfolioFactory.strategy.strategy as strategy
from ..utils import customExceptions as customExceptions


class TestStrategyFunctions(unittest.TestCase):

    def createUniverse(self,config):
        
        location = "./portfolioFactory/strategy/SampleFiles/"
        return universe.universe('test',location+config)
        

        
    def createStrategy(self,universe,config):
        
        location = "./portfolioFactory/strategy/SampleFiles/"        
        return strategy.strategy(universe,location+'strategyConfig_'+config+'.txt')
        

        
##############################################################################
# Test bad config file inputs
##############################################################################
        
    def testBadConfig_ConfigPath(self):
        # bad path for config file
        configUni = 'uni_1_5'
        configStr = 'made_up'
        testUni = self.createUniverse(configUni)
        self.assertRaises(customExceptions.invalidParameterPath,self.createStrategy,testUni,configStr)
        
        
    def testBadConfig_SignalPath(self):
        # bad path for signal file path
        configUni = 'uni_1_5'
        configStr = 'bad_signal'
        testUni = self.createUniverse(configUni)
        self.assertRaises(customExceptions.invalidSignalPath,self.createStrategy,testUni,configStr)

    def testBadConfig_MissingInput(self):
        # config file missing an input
        configUni = 'uni_1_5'
        configStr = 'missing_input'
        testUni = self.createUniverse(configUni)
        self.assertRaises(customExceptions.missingInput,self.createStrategy,testUni,configStr)
        
    def testBadConfig_UnexpectedInput(self):
        # config file encounters an unexpected input
        configUni = 'uni_1_5'
        configStr = 'extra_spec'
        testUni = self.createUniverse(configUni)
        self.assertRaises(customExceptions.unexpectedInput,self.createStrategy,testUni,configStr)
        
    def testBadConfig_StringRule(self):
        # rule parameter must be numeric
        configUni = 'uni_1_5'
        configStr = 'string_rule'
        testUni = self.createUniverse(configUni)
        self.assertRaises(customExceptions.ruleNotInt,self.createStrategy,testUni,configStr)
        
    def testBadConfig_WindowInt(self):
        # window paramter must be integer
        configUni = 'uni_1_5'
        configStr = 'string_rebalance'
        testUni = self.createUniverse(configUni)
        self.assertRaises(customExceptions.windowNotInt,self.createStrategy,testUni,configStr)
        
    def testBadConfig_WindowNeg(self):
        # window parameter must be positive
        configUni = 'uni_1_5'
        configStr = 'negative_rebalance'
        testUni = self.createUniverse(configUni)
        self.assertRaises(customExceptions.windowNegative,self.createStrategy,testUni,configStr)
        

##############################################################################
# Test mismatch between signal and returns
##############################################################################
        
    def testOverlap_Tickers(self):
        # no overlap between signal ticker and return tickers
        configUni = 'uni_1_2'
        configStr = '4_5'
        testUni = self.createUniverse(configUni)
        self.assertRaises(customExceptions.noTickerOverlap,self.createStrategy,testUni,configStr)
        
    def testOverlap_dates(self):
        # no overlap in the date spans of returns and signal
        configUni = 'uni_early'
        configStr = '1_2_late'
        testUni = self.createUniverse(configUni)
        self.assertRaises(customExceptions.noTimeOverlap,self.createStrategy,testUni,configStr)
        
##############################################################################
# Test lack of signal data
##############################################################################

    def testNoSignal(self):
        # signal data is missing, not enough obs to make selection
        configUni = 'uni_early'
        configStr = 'no_signal'
        testUni = self.createUniverse(configUni)
        self.assertRaises(customExceptions.notEnoughSignals,self.createStrategy,testUni,configStr)   
        

    

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStrategyFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)