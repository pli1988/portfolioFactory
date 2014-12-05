# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 14:02:57 2014

@author: Israel
"""
import pandas as pd

#load and drop if marketcap is missing
raw = pd.read_csv('MarketCap.csv',header=0)
mc = raw[['datadate','tic','mkvaltq']]
mc = mc[mc['mkvaltq'].notnull()]

#Format and create year and quarter columns
mc['date'] = pd.to_datetime(mc.datadate,format='%Y%m%d')
mc = mc.set_index('date')
mc['year'] = mc.index.year
mc['quarter'] = mc.index.quarter
mc = mc.reset_index(drop=True)
del mc['datadate']

#save to CSV
mc.to_csv('marketCap_clean.csv',index=False)

