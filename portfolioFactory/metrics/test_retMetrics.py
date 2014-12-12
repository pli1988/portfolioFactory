"""
test_retMetrics contains the unit tests for retMetrics module

To run all test, go to the the main ./portfolioFactory directory and run

>> python -m unittest discover

Author: Peter Li

"""

import unittest
import pandas as pd

import portfolioFactory.metrics.retMetrics as retMetrics
from ..utils import customExceptions as customExceptions

class TestRetMetricsFunctions(unittest.TestCase):
    '''Test cases for retMeterics'''

    def setUp(self):
        # Date Ranges
        self.monthRange = pd.date_range('1/1/1990', periods=20, freq='M')
        self.dayRange = pd.date_range('1/1/1990', periods=20, freq='d')
        
    def createMonthlySeries(self, value):
        # Function to create monthly series
        constSeries = pd.Series(value, index = self.monthRange)        
    
        return constSeries
        
    def createDailySeries(self, value):
        # Function to create daily series
        constSeries = pd.Series(value, index = self.dayRange)        

        return constSeries
        
##############################################################################
# Test averageHorizonReturn
##############################################################################

    def testaverageHorizonReturn_badData(self):
        # Check for data validation - file not monthly
        testSeries = self.createDailySeries(1)
        
        self.assertRaises(customExceptions.badData, retMetrics.averageHorizonReturn, testSeries, 12)

    def testaverageHorizonReturn_badDataStr(self):
        # Check for data validation - file contains str
        testSeries = self.createMonthlySeries('a')
        
        self.assertRaises(customExceptions.badData, retMetrics.averageHorizonReturn, testSeries, 12)


    def testaverageHorizonReturn_badHorizon(self):
        # Quick check of data validation, main check will be in test of util.trim
        testSeries = self.createMonthlySeries(0.5)
        
        self.assertRaises(customExceptions.invalidInput, retMetrics.averageHorizonReturn, testSeries, 0.5)

    def testaverageHorizonReturn_Constant(self):
        # Given constant positive values, average should be value cumulated over period
        testSeries = self.createMonthlySeries(0.5)

        self.assertEqual(retMetrics.averageHorizonReturn(testSeries,1), 0.5)
        self.assertEqual(retMetrics.averageHorizonReturn(testSeries,5), (1+0.5)**5 -1)

##############################################################################
# Test cumulativeReturn
##############################################################################

    def testcumulativeReturn_invalidInput(self):
        # Check for data validation - file not monthly
        testSeries = self.createDailySeries(1)
        
        self.assertRaises(customExceptions.badData, retMetrics.cumulativeReturn, testSeries)
        
    def testcumulativeReturn_Constant(self):
        # Given constant positive values, cumulative return is (1+value)^length -1
        testSeries = self.createMonthlySeries(0.5)

        self.assertEqual(retMetrics.cumulativeReturn(testSeries), (1+0.5)**len(testSeries)-1)
        
##############################################################################
# Test Rolling Return
##############################################################################

    def testrollingReturn_badData(self):
        # Check for data validation - file not monthly
        testSeries = self.createDailySeries(1)
        
        self.assertRaises(customExceptions.badData, retMetrics.rollingReturn, testSeries, 12)

    def testrollingReturn_badHorizon(self):
        # Check for data validation - file not monthly
        testSeries = self.createMonthlySeries(0.5)
        
        self.assertRaises(customExceptions.invalidInput, retMetrics.rollingReturn, testSeries, 0.5)   
 
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRetMetricsFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)