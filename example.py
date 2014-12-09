# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 22:53:50 2014

@author: peter
"""


import portfolioFactory.universe.universe as universe
import portfolioFactory.utils.utils as utils    
import portfolioFactory.metrics.riskMetrics as riskMetrics
import portfolioFactory.metrics.retMetrics as retMetrics

# Create Instance of universe for US Equities
#usEqUniverse = universe.universe('portfolioFactory/universe/usEquityConfig.txt')

try:
    usEqUniverse = universe.universe('portfolioFactory/universe/usEquityConfig.txt')
except:
    print 'Error: Could not initialize universe'
    raise

    
    
testSeries = usEqUniverse.assetReturns.GS

utils.checkSeqentialMonthly(testSeries)

riskMetrics.maxDrawdown(testSeries)
riskMetrics.VaR(testSeries, 12, .95)
retMetrics.rollingReturn(testSeries, 6).plot()


# Get Summary Statistics
usEqUniverse.computeSummary()

# Plot Return
usEqUniverse.assetReturns.A.plot()



