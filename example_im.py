# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 21:50:31 2014

@author: Israel
"""

import pandas as pd
import cPickle as pickle


def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


#file name is text.pkl

import portfolioFactory
import portfolioFactory.universe.universe as universe
import portfolioFactory.strategy.strategy as strategy
import portfolioFactory.portfolio.portfolio as portfolio
from   portfolioFactory.utils import customExceptions as customExceptions

location = "portfoliofactory/strategy/SampleFiles/"

testUni = universe.universe('testUni',location+'uni_base')
testStrategy = strategy.strategy(testUni,location+'strategyConfig_1_2.txt')
testStrategy2 = strategy.strategy(testUni,location+'strategyConfig_1_2.txt')
testStrategy.parameters['name'] = 'USEquityStrategy02'
testPort = portfolio.portfolio([testStrategy,testStrategy2],[3,7])


#save_object(testStrategy,'testStrategy')
#save_object(testPort,'testPort')