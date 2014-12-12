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


#def plotRollingReturn(data):
#    
#    fig, axes = plt.subplots(4, sharex = True, figsize=(8, 8))
#    
#    retMetrics.rollingReturn(data,3).plot(ax = axes[0])
#    retMetrics.rollingReturn(data,6).plot(ax = axes[1])
#    retMetrics.rollingReturn(data,12).plot(ax = axes[2])
#    retMetrics.rollingReturn(data,24).plot(ax = axes[3])
#    
#    axes[0].set_xlabel('')
#    axes[1].set_xlabel('')
#    axes[2].set_xlabel('')
#    
#    
#    
#    axes[0].set_title('Rolling 3-Month Return')
#    axes[1].set_title('Rolling 6-Month Return')
#    axes[2].set_title('Rolling 1-Year Return')
#    axes[3].set_title('Rolling 2-Year Return')
#    
#    
#    fig.show()


def plotRollingReturn(data):
       
    ax1 = plt.subplot2grid((4,3), (0,0), colspan = 2)
    ax2 = plt.subplot2grid((4,3), (1,0), colspan = 2)
    ax3 = plt.subplot2grid((4,3), (2,0), colspan = 2)
    ax4 = plt.subplot2grid((4,3), (3,0), colspan = 2)    
        
    ax5 = plt.subplot2grid((4,3), (0,2), colspan = 1, xlim = (-1,1))
    ax6 = plt.subplot2grid((4,3), (1,2), colspan = 1, xlim = (-1,1))
    ax7 = plt.subplot2grid((4,3), (2,2), colspan = 1, xlim = (-1,1))
    ax8 = plt.subplot2grid((4,3), (3,2), colspan = 1, xlim = (-1,1))
    
    
    current_palette = sns.color_palette("Blues")

    retMetrics.rollingReturn(data,3).plot(ax = ax1, color = current_palette[2])
    retMetrics.rollingReturn(data,6).plot(ax = ax2, color = current_palette[3])
    retMetrics.rollingReturn(data,12).plot(ax = ax3, color = current_palette[4])
    retMetrics.rollingReturn(data,24).plot(ax = ax4, color = current_palette[5])

    retMetrics.rollingReturn(data,3).hist(ax = ax5, bins = 30, color = current_palette[2])
    retMetrics.rollingReturn(data,6).hist(ax = ax6, bins = 30, color = current_palette[3])
    retMetrics.rollingReturn(data,12).hist(ax = ax7, bins = 30, color = current_palette[4])
    retMetrics.rollingReturn(data,24).hist(ax = ax8, bins = 30, color = current_palette[5])
    
    ax1.set_xlabel('')
    ax2.set_xlabel('')
    ax3.set_xlabel('')
    
    ax1.get_xaxis().set_ticks([])
    ax2.get_xaxis().set_ticks([])
    ax3.get_xaxis().set_ticks([])
    
    ax1.set_title('Rolling Returns', fontsize = 15)
    
    ax1.set_ylabel('3 Months', fontsize = 15)
    ax2.set_ylabel('6 Months', fontsize = 15)
    ax3.set_ylabel('1 Year', fontsize = 15)
    ax4.set_ylabel('2 Years', fontsize = 15)    
    
    ax5.set_title('Distribution of Rolling Returns', fontsize = 15)

plotRollingReturn(usEqUniverse.assetReturns.GS)


from pandas.tools.plotting import bootstrap_plot

bootstrap_plot(testSeries, size=50, samples=500, color='green')

# Metrics
utils.checkSeqentialMonthly(testSeries.index)
riskMetrics.maxDrawdown(testSeries)

riskMetrics.VaR(testSeries, 12, 95)
retMetrics.rollingReturn(testSeries, 6).plot()


# Get Summary Statistics

usEqUniverse.computeSummary()

