# -*- coding: utf-8 -*-

class portfolio(object):
    
    '''

    A class to represent portfolios
    
    '''
    
    def __init__(self,universe,strategy):
        
        self.universe = universe.returns.copy()
        self.weights = strategy.weights.copy()
        self.portfolio = self.__genPortfolio()
        
    def __genPortfolio(self):
        weights = self.weights.copy()
        returns = self.universe
        weights['rebal'] = 1
        merged = pd.merge(returns,weights,how='left',left_index=True,right_index=True,suffixes=['_r','_w'])
        merged['flip'] = None
        merged['flip'][merged.rebal==1] = np.arange((merged.rebal==1).sum())
        merged['flip'] = merged['flip'].fillna(method='ffill')
        return merged
        
testPort = portfolio(testUniverse,testStrategy)
        
        


glbstart=1
def rebal(df,r,w):
    global glbstart
    
    return all
    
'''