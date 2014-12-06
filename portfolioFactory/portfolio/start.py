# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 23:59:27 2014

@author: Israel
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data into a pandas dataframe
rawDf = pd.read_csv('stockprices.csv')

# Clean up data a little
rawDf.datadate = pd.to_datetime(rawDf.datadate,format = '%Y%m%d')
rawDf.trt1m = rawDf.trt1m / 100

# turn serialized data into a panel
returnPanel = rawDf.pivot(index='datadate', columns='tic', values='trt1m')
#returnPanel = returnPanel[returnPanel.columns[0:5]]

#generate a DF of weights
wcols = ['w_'+x for x in returnPanel.columns]
windex = returnPanel.index[0:len(returnPanel.index):6]
wdata = pd.DataFrame(np.random.uniform(0,1,len(wcols)*len(windex)).reshape(len(windex),len(wcols)))
wdata = wdata.T.apply(lambda x:x/x.sum()).T
weights = pd.DataFrame(wdata.values,columns=wcols,index=windex)
weights['rebal']=1


#write a module that will create returns

#1 merge weights and returns
data = pd.merge(returnPanel,weights,how='outer',left_index=True,right_index=True)

#empty(Nan) returns are the same as zero
data[returnPanel.columns]=data[returnPanel.columns].fillna(0)

#generate weight-groupings
data['chunk']=None
data['chunk'][data.rebal==1] = np.arange((data.rebal==1).sum())
data['chunk']=data['chunk'].fillna(method='ffill')



glbstart=1
def rebal(df,r,w):
    global glbstart
    ind = pd.DataFrame((1+df[r])*np.array(df[w].min()))
    port = pd.DataFrame(ind.sum(axis=1),columns=["Port"])
    all = pd.merge(ind,port,left_index=True,right_index=True)
    return all