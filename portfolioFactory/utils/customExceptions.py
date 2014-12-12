# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 12:38:21 2014

@author: Israel
"""

class invalidParameterPath(Exception) :
        def __init__(self,msg='') :
            self.m="The specified config path did not return a pickled dataframe:"+str(msg)
        def __str__(self):
            return repr(self.m)
            
class invalidSignalPath(Exception) :
        def __init__(self,msg='') :
            self.m="The specified signal path did not return a pickled dataframe:"+str(msg)
        def __str__(self):
            return repr(self.m)
            
class missingInput(Exception) :
        def __init__(self,msg='') :
            self.m="Config file is missing an input:"+str(msg)
        def __str__(self):
            return repr(self.m)
            
class unexpectedInput(Exception) :
        def __init__(self,msg='') :
            self.m="Config file encountered unexpected input:"+str(msg)
        def __str__(self):
            return repr(self.m)
            
class windowNotInt(Exception) :
        def __init__(self,msg='') :
            self.m="Window parameter must be integer: passed  "+str(msg)
        def __str__(self):
            return repr(self.m)

class windowNegative(Exception) :
        def __init__(self,msg='') :
            self.m="Window parameter must be positive: passed  "+str(msg)
        def __str__(self):
            return repr(self.m)
            
class ruleNotInt(Exception) :
        def __init__(self,msg='') :
            self.m="Rule parameter must be integer: passed  "+str(msg)
        def __str__(self):
            return repr(self.m)
            
class noTimeOverlap(Exception) :
        def __init__(self,msg='') :
            self.m="Singal data and universe.assetReturns dates do not overlap"
        def __str__(self):
            return repr(self.m)
            
class noTickerOverlap(Exception) :
        def __init__(self,msg='') :
            self.m="Singal data and universe.assetReturns tickers do not intersect"
        def __str__(self):
            return repr(self.m)
            
class notEnoughSignals(Exception) :
        def __init__(self,msg='') :
            self.m="Signal data does not have enough non-Nan values to make selection at specified rule for "+str(msg)+" periods"
        def __str__(self):
            return repr(self.m)
            
            
###################################################
            
class notListError(Exception) :
        def __init__(self,msg='') :
            self.m="Both strategyPool argument and weights argument must be lists"
        def __str__(self):
            return repr(self.m)
            
class listMismatchError(Exception) :
        def __init__(self,msg='') :
            self.m="strategyPool and weights must contain the same number of elements"
        def __str__(self):
            return repr(self.m)
            
class notStrategyError(Exception) :
        def __init__(self,msg='') :
            self.m="strategyPool must be a list of strategy objects"
        def __str__(self):
            return repr(self.m)
            
class badWeightError(Exception) :
        def __init__(self,msg='') :
            self.m="weights must be a list of numeric weights"
        def __str__(self):
            return repr(self.m)
            
class duplicatesError(Exception) :
        def __init__(self,msg='') :
            self.m="Two strategies with the same name (in parameters dictionary) were passed"
        def __str__(self):
            return repr(self.m)
            
######################################################
            
class notDFError(Exception) :
        def __init__(self,msg='') :
            self.m="First input must be a pandas dataframe"
        def __str__(self):
            return repr(self.m)    
            
            
            
            
            

            
            
