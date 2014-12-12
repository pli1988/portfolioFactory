# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 22:53:50 2014

Author: Peter Li
"""


import portfolioFactory.universe.universe as universe


import portfolioFactory.utils.utils as utils    
import portfolioFactory.metrics.riskMetrics as riskMetrics
import portfolioFactory.metrics.retMetrics as retMetrics

import portfolioFactory.strategy.strategy as strategy
import portfolioFactory.portfolio.portfolio as portfolio
import portfolioFactory.reporting.reporting as reporting

#from portfolioFactory.utils import getFileLocation

#assetReturnsPath = getFileLocation.getFileLocation()
#configFilePath = getFileLocation.getFileLocation()


assetReturnsPath = './portfolioFactory/universe/totalReturnData' 
usEqUniverse = universe.universe('testUniverse', assetReturnsPath)

configFilePath = './portfolioFactory/strategy/SampleFiles/strategyConfig_1_5.txt'
testStrategy = strategy.strategy(usEqUniverse, configFilePath)

testPortfolio =  portfolio.portfolio([testStrategy],[1]) 

###############################################################################
# Plotting
###############################################################################

testSeries = testStrategy.strategyReturns
    


reporting.plotRollingReturn(usEqUniverse.assetReturns.GS)


from pandas.tools.plotting import bootstrap_plot

bootstrap_plot(testSeries, size=50, samples=500, color='green')

# Metrics
utils.checkSeqentialMonthly(testSeries.index)
riskMetrics.maxDrawdown(testSeries)

riskMetrics.VaR(testSeries, 12, 95)
retMetrics.rollingReturn(testSeries, 6).plot()


# Get Summary Statistics

usEqUniverse.computeSummary()

