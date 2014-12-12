# -*- coding: utf-8 -*-
"""
@author: Israel
"""

''' Module to preform unit tests on strategy class

'''
    
import pandas as pd
import numpy as np
from portfolioFactory.universe import universe as universe
from portfolioFactory.strategy import strategy as strategy
from portfolioFactory.utils.utils import calcRollingReturns as calcRollingReturns

location = "portfoliofactory/strategy/SampleFiles/"


# pickle subsets of the full data
allData = pd.read_pickle(location+'totalReturnData')
allData[['AA','BA','IBM','HPQ','INT']].to_pickle(location+'uni_1_5')
allData[['AA','BA']].to_pickle(location+'uni_1_2')
allData[['HPQ','INT']].to_pickle(location+'uni_4_5')


uni_1_5 = universe.universe(location+'config_uni_1_5.txt')
signal_1_5 = calcRollingReturns(uni_1_5.assetReturns,6).shift(period=1)
signal_1_5_early = signal_1_5.truncate(before="01/01/1996",after="31/12/2005")
signal_1_5_late = signal_1_5.truncate(before="01/01/2006",after="31/12/2012")

uni_1_2 = universe.universe(location+'config_uni_1_2.txt')
signal_1_2 = calcRollingReturns(uni_1_2.assetReturns,6).shift(period=1)
signal_1_2_early = signal_1_2.truncate(before="01/01/1996",after="31/12/2005")
signal_1_2_late = signal_1_2.truncate(before="01/01/2006",after="31/12/2012")

uni_4_5 = universe.universe(location+'config_uni_4_5.txt')
signal_4_5 = calcRollingReturns(uni_4_5.assetReturns,6).shift(period=1)
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

### this one should raise notickeroverlap
stra_ticker= strategy.strategy(uni_1_2,location+'strategyConfig_4_5.txt')

### this one should raise date overlap error
uni_1_2.assetReturns = signal_1_2_early
stra_time= strategy.strategy(uni_1_2,location+'strategyConfig_1_2_late.txt')

### this one should raise missing input error
stra_time= strategy.strategy(uni_1_2,location+'strategyConfig_missing_input.txt')

### this one should raise unexpected input error
stra_time= strategy.strategy(uni_1_2,location+'strategyConfig_extra_spec.txt')

### this one should raise bad config path
stra_time= strategy.strategy(uni_1_2,location+'strategyConfig_does_not_exist.txt')

### this one should raise bad signal path
stra_time= strategy.strategy(uni_1_2,location+'strategyConfig_bad_signal.txt')

### this one should raise non-numeric rebalanceWindow
stra_time= strategy.strategy(uni_1_2,location+'strategyConfig_string_rebalance.txt')

### this one should raise negative rebalanceWindow
stra_time= strategy.strategy(uni_1_2,location+'strategyConfig_negative_rebalance.txt')

### this one should raise string rule
stra_time= strategy.strategy(uni_1_2,location+'strategyConfig_string_rule.txt')

### checking rebalncing calculation
uni_4_5.assetReturns[['HPQ']] = np.ones((uni_4_5.assetReturns.shape[0],1))
uni_4_5.assetReturns[['INT']] = np.ones((uni_4_5.assetReturns.shape[0],1))/2
stra_time= strategy.strategy(uni_4_5,location+'strategyConfig_rebal_check.txt')


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