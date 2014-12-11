# -*- coding: utf-8 -*-
"""
@author: Israel
"""

''' Module to preform unit tests on strategy class

'''
    
import pandas as pd
import numpy as np
import portfolioFactory
from portfolioFactory.universe import universe as universe
from portfolioFactory.strategy import strategy as strategy
from portfolioFactory.utils import calcRollingReturns as calcRollingReturns
from portfolioFactory.utils import setParameters as setParameters
from portfolioFactory.exceptions.exceptions import *

location = "portfoliofactory/strategy/SampleFiles/"


# pickle subsets of the full data
allData = pd.read_pickle(location+'totalReturnData')
allData[['AA','BA','IBM','HPQ','INT']].to_pickle(location+'uni_1_5')
allData[['AA','BA']].to_pickle(location+'uni_1_2')
allData[['HPQ','INT']].to_pickle(location+'uni_4_5')


uni_1_5 = universe.universe(location+'config_uni_1_5.txt')
signal_1_5 = calcRollingReturns.calcRollingReturns(uni_1_5.assetReturns,6).shift(period=1)
signal_1_5_early = signal_1_5.truncate(before="01/01/1996",after="31/12/2005")
signal_1_5_late = signal_1_5.truncate(before="01/01/2006",after="31/12/2012")

uni_1_2 = universe.universe(location+'config_uni_1_2.txt')
signal_1_2 = calcRollingReturns.calcRollingReturns(uni_1_2.assetReturns,6).shift(period=1)
signal_1_2_early = signal_1_2.truncate(before="01/01/1996",after="31/12/2005")
signal_1_2_late = signal_1_2.truncate(before="01/01/2006",after="31/12/2012")

uni_4_5 = universe.universe(location+'config_uni_4_5.txt')
signal_4_5 = calcRollingReturns.calcRollingReturns(uni_4_5.assetReturns,6).shift(period=1)
signal_4_5_early = signal_4_5.truncate(before="01/01/1996",after="31/12/2005")
signal_4_5_late = signal_4_5.truncate(before="01/01/2006",after="31/12/2012")

pd.to_pickle(signal_1_5,location+'signal_1_5')
pd.to_pickle(signal_1_5_early,location+'signal_1_5_early')
pd.to_pickle(signal_1_5_late,location+'signal_1_5_late')
pd.to_pickle(signal_1_2,location+'signal_1_2')
pd.to_pickle(signal_1_2_early,location+'signal_1_2_early')
pd.to_pickle(signal_1_2_late,location+'signal_1_2_late')
pd.to_pickle(signal_4_5,location+'signal_4_5')
pd.to_pickle(signal_4_5_early,location+'signal_4_5_early')
pd.to_pickle(signal_4_5_late,location+'signal_4_5_late')


### this one should work well
stra_well = strategy.strategy(uni_1_5,location+'strategyConfig_1_5_late.txt')


'''
class TestmergeIntervals(unittest.TestCase):
    def setUp(self):
        self.itema = interval("[5,10]")
	   self.itemb = interval("(5,10)")
        self.mymerge = mergeIntervals(self.itema,self.itemb)
    def test_interior(self):
        self.assertEqual(self.mymerge.leftreal, self.itema.leftreal)

if __name__ == '__main__':
    unittest.main()
 '''