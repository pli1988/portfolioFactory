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

from portfolioFactory.utils import getFileLocation

# Create Instance of universe for US Equities
#usEqUniverse = universe.universe('portfolioFactory/universe/usEquityConfig.txt')


#assetReturnsPath = getFileLocation.getFileLocation()


#configFilePath = getFileLocation.getFileLocation()


assetReturnsPath = '/home/peter/Documents/Homework/ProgrammingForDatascience/finalProject2/portfolioFactory/portfolioFactory/universe/totalReturnData' 
configFilePath = '/home/peter/Documents/Homework/ProgrammingForDatascience/finalProject2/portfolioFactory/portfolioFactory/strategy/SampleFiles/strategyConfig_1_5.txt'


usEqUniverse = universe.universe('testUniverse', assetReturnsPath)
testStrategy = strategy.strategy(usEqUniverse, configFilePath)
testPortfolio =  portfolio.portfolio([testStrategy],[1]) 

###############################################################################
# Plotting
###############################################################################

testSeries = testStrategy.strategyReturns


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
np.random.seed(sum(map(ord, "aesthetics")))

import seaborn as sns

txt = '''
    Lorem ipsum dolor sit amet, consectetur adipisicing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
    reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
    pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
    culpa qui officia deserunt mollit anim id est laborum.'''
    
    
f, axarr = plt.subplots(3, sharex = True)

axarr[0].plot(testSeries.index,retMetrics.rollingReturn(testSeries,12), 'r')
axarr[1].plot(testSeries.index,retMetrics.rollingReturn(testSeries,36), 'g')
axarr[2].plot(testSeries.index,retMetrics.rollingReturn(testSeries,60))

#
#f.text(.1,.1,txt)
f.show()

fig, axes = plt.subplots(3, sharex = True)

retMetrics.rollingReturn(testSeries,12).plot(ax = axes[0])
retMetrics.rollingReturn(testSeries,36).plot(ax = axes[1])
retMetrics.rollingReturn(testSeries,50).plot(ax = axes[2])

axes[0].set_xlabel('')
axes[1].set_xlabel('')

axes[0].set_title('Rolling 1-Year Return')
axes[1].set_title('Rolling 3-Year Return')
axes[2].set_title('Rolling 5-Year Return')

fig.show()


# Metrics
utils.checkSeqentialMonthly(testSeries.index)
riskMetrics.maxDrawdown(testSeries)

riskMetrics.VaR(testSeries, 12, 95)
retMetrics.rollingReturn(testSeries, 6).plot()


# Get Summary Statistics

usEqUniverse.computeSummary()

# Plot Return
usEqUniverse.assetReturns.A.plot()



import portfolioFactory.metrics.test_riskMetrics as test_riskMetrics