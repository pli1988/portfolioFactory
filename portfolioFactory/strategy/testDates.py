# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 22:35:34 2014

@author: Israel
"""
import pandas as pd
mc=pd.read_csv('MarketCap/marketCap_clean.csv',index_col=0,header=0,parse_dates=True)
mc=mc[mc['tic'].isin(['AAPL','GOOGL','MSFT','DELL','MS','BAC','C'])]
mc = mc.pivot_table(index=mc.index,columns='tic',values='mkvaltq')

emp = pd.DataFrame(index=mc.index,columns=mc.columns)