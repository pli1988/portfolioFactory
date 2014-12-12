"""
Example01 is a module to run the first of three examples showing what portfolioFactory can do

Author: Israel Malkin
"""

import pandas as pd
import portfolioFactory
import portfolioFactory.universe.universe as universe
import portfolioFactory.strategy.strategy as strategy
import portfolioFactory.portfolio.portfolio as portfolio
import portfolioFactory.plottingIM.plotWithStats as plot
from   portfolioFactory.utils.utils import calcRollingReturns


location = './ExampleFiles/'


universe_Ex1 = universe.universe('Universe_Ex1',location+'totalReturnData')
rollingReturns_Ex1 = calcRollingReturns(universe_Ex1.assetReturns,12).shift(period=1).truncate(before="01/01/1999",after="31/01/2009")
rollingReturns_Ex1.to_pickle(location+'signal_Ex1')
strategy_Ex1 = strategy.strategy(universe_Ex1,location+'config_Ex1.txt')

plot(strategy_Ex1.strategyReturns,2001,2008)

universe_Ex2 = universe.universe('Universe_Ex2',location+'totalReturnData')
rollingReturns_Ex2 = calcRollingReturns(universe_Ex2.assetReturns,6).shift(period=1).truncate(before="01/01/1999",after="31/01/2009")
rollingReturns_Ex2.to_pickle(location+'signal_Ex2')
strategy_Ex2 = strategy.strategy(universe_Ex2,location+'config_Ex2.txt')



universe_Ex3 = universe.universe('Universe_Ex3',location+'totalReturnData')
rollingReturns_Ex3 = pd.rolling_std(universe_Ex3.assetReturns,60).shift(period=1).truncate(before="01/01/1999",after="31/01/2009")
rollingReturns_Ex3.to_pickle(location+'signal_Ex3')
strategy_Ex3 = strategy.strategy(universe_Ex3,location+'config_Ex3.txt')

portfolio = portfolio.portfolio([strategy_Ex1,strategy_Ex2],[1,1])