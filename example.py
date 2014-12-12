

import unittest
import pandas as pd

import portfolioFactory.universe.universe as universe
import portfolioFactory.strategy.strategy as strategy
import portfolioFactory.portfolio.portfolio as portfolio



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
           