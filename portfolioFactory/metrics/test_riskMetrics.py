"""
test_riskMetrics contains the unit tests for riskMetrics module

To run all test, go to the the main ./portfolioFactory directory and run

>> python -m unittest discover

Author: Peter Li

"""

import unittest
import pandas as pd

import portfolioFactory.metrics.riskMetrics as riskMetrics
from ..utils import customExceptions as customExceptions


class TestRiskMetricsFunctions(unittest.TestCase):
    '''Test cases for retMeterics'''

    def setUp(self):
        # Date ranges
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
# Test maxDrawdown
##############################################################################

    def testDrawdown_invalidInput(self):
        # Quick check of data validation, main check will be in test of util.trim
        testSeries = self.createDailySeries(1)
        
        self.assertRaises(customExceptions.badData, riskMetrics.maxDrawdown, testSeries)

    def testDrawdown_invalidInputStr(self):
        # Quick check of data validation, main check will be in test of util.trim
        testSeries = self.createMonthlySeries('a')
        
        self.assertRaises(customExceptions.badData, riskMetrics.maxDrawdown, testSeries)
        
    def testDrawDown_ConstantPositive(self):
        # Given constant positive values, drawdown is 0
        testSeries = self.createMonthlySeries(0.5)

        self.assertEqual(riskMetrics.maxDrawdown(testSeries), 0)    

    def testDrawDown_ConstantNegative(self):
        # Given constant negative values, drawdown is (1+value)^length -1
        testSeries = self.createMonthlySeries(-0.5)

        self.assertEqual(riskMetrics.maxDrawdown(testSeries), (-0.5)**len(self.monthRange)-1)           
 
    def testDrawDown_middle(self):
        # Given 2 periods of consecutive negative values, all else nonnegative, drawdown is product
        testSeries = self.createMonthlySeries(0.1)
        
        testSeries.ix[4] = -0.5
        testSeries.ix[5] = -0.4

        self.assertEqual(riskMetrics.maxDrawdown(testSeries), ((1 - 0.5)*(1 - 0.4))-1)           
           
##############################################################################
# Test annualizedVolatility
##############################################################################

    def testVol_invalidInput(self):
        # Quick check of data validation, main check will be in test of util.trim
        testSeries = self.createDailySeries(1)
        
        self.assertRaises(customExceptions.badData, riskMetrics.annualizedVolatility, testSeries)


    def testVol_invalidInputStr(self):
        # Quick check of data validation, main check will be in test of util.trim
        testSeries = self.createMonthlySeries('a')
        
        self.assertRaises(customExceptions.badData, riskMetrics.annualizedVolatility, testSeries)


    def testVol_ConstantPositive(self):
        # Given constant positive values, vol is 0
        testSeries = self.createMonthlySeries(0.5)

        self.assertEqual(riskMetrics.annualizedVolatility(testSeries), 0)    
        
    def testVol_ConstantNegative(self):
        # Given constant negative values, vol is 0
        testSeries = self.createMonthlySeries(-0.5)

        self.assertEqual(riskMetrics.annualizedVolatility(testSeries), 0)  

##############################################################################
# Test VaR
##############################################################################

    def testVaR_badData(self):
        # Quick check of data validation, main check will be in test of util.trim
        testSeries = self.createDailySeries(1)
        
        self.assertRaises(customExceptions.badData, riskMetrics.VaR, testSeries, 12, 90)

    def testVaR_badDataStr(self):
        # Quick check of data validation, main check will be in test of util.trim
        testSeries = self.createDailySeries('a')
        
        self.assertRaises(customExceptions.badData, riskMetrics.VaR, testSeries, 12, 90)

    def testVaR_badHorizon(self):
        # Quick check of data validation, main check will be in test of util.trim
        testSeries = self.createMonthlySeries(0.5)
        
        self.assertRaises(customExceptions.invalidInput, riskMetrics.VaR, testSeries, 0.5, 9)

    def testVaR_badProbability(self):
        # Quick check of data validation, main check will be in test of util.trim
        testSeries = self.createMonthlySeries(0.5)
        
        self.assertRaises(customExceptions.invalidInput, riskMetrics.VaR, testSeries, 12, 120)

    def testVaR_ConstantPositive(self):
        # Given constant positive values, vol is 0
        testSeries = self.createMonthlySeries(0.5)

        self.assertEqual(riskMetrics.VaR(testSeries, 12, 90), (1+0.5)**12 -1)    
 
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRiskMetricsFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)