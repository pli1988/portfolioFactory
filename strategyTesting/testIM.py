# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 15:35:49 2014

@author: Israel
"""

import portfolioFactory
import portfolioFactory.universe.universe as universe
import portfolioFactory.strategy.strategy as strategy
import portfolioFactory.portfolio.portfolio as portfolio
from portfolioFactory.utils.calcRollingReturns import *
import datetime




testUni01 = universe.universe('strategyTesting/universeConfig.txt')
testSignal01 = calcRollingReturns(testUni01.assetReturns,6).shift(period=1)[['AA','BA','IBM','HPQ','INT']].truncate(before="01/01/1995",after="31/12/2012")
testSignal01.to_pickle('strategyTesting/testSignal01')
#testSignal02 = calcRollingReturns(testUni01.assetReturns,6).shift(period=1)[['AA','BA','IBM','HPQ','INT']].truncate(before="01/01/1995",after="31/12/2012")
#testSignal02.to_pickle('testSignal02')
testStr01 = strategy.strategy(testUni01,'strategyTesting/strategyConfig01.txt')
testStr02 = strategy.strategy(testUni01,'strategyTesting/strategyConfig02.txt')

testPort = portfolio.portfolio([testStr01,testStr02],[1,1])


