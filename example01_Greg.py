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
rolling_returns_12m = calcRollingReturns(universe_Ex1.assetReturns,12).shift(period=1).truncate(before="01/01/1995",after="31/01/2012")
rolling_volatility_24m = pd.rolling_std(universe_Ex1.assetReturns,24).shift(period=1).truncate(before="01/01/1995",after="31/01/2012")

rolling_returns_12m.to_pickle(location+'rolling_returns_12m')
rolling_volatility_24m.to_pickle(location+'rolling_volatility_24m')