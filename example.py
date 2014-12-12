

import unittest
import pandas as pd

import portfolioFactory.universe.universe as universe
import portfolioFactory.strategy.strategy as strategy
import portfolioFactory.portfolio.portfolio as portfolio
from portfolioFactory.utils import getFileLocation

# Create Instance of universe for US Equities
#usEqUniverse = universe.universe('portfolioFactory/universe/usEquityConfig.txt')


assetReturnsPath = getFileLocation.getFileLocation()


#configFilePath = getFileLocation.getFileLocation()


assetReturnsPath = '/home/peter/Documents/Homework/ProgrammingForDatascience/finalProject2/portfolioFactory/portfolioFactory/universe/totalReturnData' 
configFilePath = '/home/peter/Documents/Homework/ProgrammingForDatascience/finalProject2/portfolioFactory/portfolioFactory/strategy/SampleFiles/strategyConfig_1_5.txt'


usEqUniverse = universe.universe('testUniverse', assetReturnsPath)
testStrategy = strategy.strategy(usEqUniverse, configFilePath)
testPortfolio =  portfolio.portfolio([testStrategy],[1])

    
    



testSeries = testStrategy.strategyReturns

utils.checkSeqentialMonthly(testSeries.index)
riskMetrics.maxDrawdown(testSeries)
riskMetrics.VaR(testSeries, 12, 95)
retMetrics.rollingReturn(testSeries, 6).plot()


# Get Summary Statistics

usEqUniverse.computeSummary()

# Plot Return
usEqUniverse.assetReturns.A.plot()

def createUniverse(config):
        
        location = "portfoliofactory/strategy/SampleFiles/"
        return universe.universe(location+'config_'+config+'.txt')
        
        
def createStrategy(universe,config):
        
        location = "portfoliofactory/strategy/SampleFiles/"        
        return strategy.strategy(universe,location+'strategyConfig_'+config+'.txt')
        
def createPortfolio(a,b):
        
        return portfolio.portfolio(a,b)


configUni = 'uni_early'
configStr = '1_5'
testUni = createUniverse(configUni)
testStr1 = createStrategy(testUni,configStr)
testStr2 = createStrategy(testUni,configStr) 
testStr2.parameters['name']='other'
      
a = [testStr1,testStr2]
b = [1,1]
c=createPortfolio(a,b)
           
