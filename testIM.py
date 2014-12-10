# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 15:35:49 2014

@author: Israel
"""

import portfolioFactory
import portfolioFactory.universe.universe as universe
import portfolioFactory.strategy.strategy as strategy
from portfolioFactory.utils.calcRollingReturns import *
import datetime

first = datetime.datetime.now()


testUni01 = universe.universe('universeConfig01.txt')
#testSignal01 = calcRollingReturns(testUni01.assetReturns,6)[['AA','BA','IBM','HPQ','INT']].truncate(before="01/01/1990",after="31/12/2012")
testSignal01 = calcRollingReturns(testUni01.assetReturns,6).shift(period=1).truncate(before="01/01/1997",after="31/12/2012")
testSignal01.to_pickle('testSignal01')
testStr01 = strategy.strategy(testUni01,'strategyConfig01.txt')


second = datetime.datetime.now()

print second-first