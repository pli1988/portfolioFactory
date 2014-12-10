# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 22:53:50 2014

Author: Peter Li
"""


import portfolioFactory.universe.universe as universe


import portfolioFactory.utils.utils as utils    
import portfolioFactory.metrics.riskMetrics as riskMetrics
import portfolioFactory.metrics.retMetrics as retMetrics

# Create Instance of universe for US Equities
#usEqUniverse = universe.universe('portfolioFactory/universe/usEquityConfig.txt')


usEqUniverse = universe.universe('testUniverse')
    
    
testSeries = usEqUniverse.assetReturns.GS

utils.checkSeqentialMonthly(testSeries)

riskMetrics.maxDrawdown(testSeries)
riskMetrics.VaR(testSeries, 12, .95)
retMetrics.rollingReturn(testSeries, 6).plot()


# Get Summary Statistics
usEqUniverse.computeSummary()

# Plot Return
usEqUniverse.assetReturns.A.plot()



import portfolioFactory.metrics.test_riskMetrics as test_riskMetrics