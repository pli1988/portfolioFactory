"""
reporting is a module that contains a collection of functions to make plots

Author: Peter Li

"""



from ..utils import utils as utils
from ..utils import customExceptions as customExceptions


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import portfolioFactory.metrics.retMetrics as retMetrics

#np.random.seed(sum(map(ord, "aesthetics")))


current_palette = sns.color_palette("Blues")

def plotRollingReturn(inputData, windowArray):
    '''Plots a panel of 4 rolling returns and histogram
    
    Note: size fixed to allow for nicer looking graphs
    
    Input:
        - inputData (timeseries): timeseries of monthly returns
        - horizon (list): list of 4 integers for rolling analysis 
    
    '''
        
    # check in windowArray is a list of 4 integers
    listCheck = isinstance(windowArray, list)
    lengthCheck = len(windowArray) == 4
    typeCheck = all([isinstance(x, int) for x in windowArray ])
        
    if all([listCheck, lengthCheck, typeCheck]):
        sns.set_context("paper")
        
        data = utils.processData(inputData)
        
        fig = plt.figure(figsize=(16, 8))
        fig.patch.set_facecolor('white') 
    
        # Create axis for subplots
        ax1 = plt.subplot2grid((4,3), (0,0), colspan = 2)
        ax2 = plt.subplot2grid((4,3), (1,0), colspan = 2)
        ax3 = plt.subplot2grid((4,3), (2,0), colspan = 2)
        ax4 = plt.subplot2grid((4,3), (3,0), colspan = 2)    
            
        ax5 = plt.subplot2grid((4,3), (0,2), colspan = 1)
        ax6 = plt.subplot2grid((4,3), (1,2), colspan = 1)
        ax7 = plt.subplot2grid((4,3), (2,2), colspan = 1)
        ax8 = plt.subplot2grid((4,3), (3,2), colspan = 1)
        
        tsAx = [ax1, ax2, ax3, ax4]
        histAx = [ax5, ax6, ax7, ax8]
        
        # Plot rolling returns and histograms
        for ixWindow in range(4):        
            
            ixColor = current_palette[2+ixWindow]
            retMetrics.rollingReturn(data,windowArray[ixWindow]).plot(ax = tsAx[ixWindow], color = ixColor)
            retMetrics.rollingReturn(data,windowArray[ixWindow]).hist(ax = histAx[ixWindow], bins = 30, color = ixColor)
            tsAx[ixWindow].set_ylabel(str(windowArray[ixWindow]) + ' Months', fontsize = 15)
        
        # remove lables for ts plots
        ax1.set_xlabel('')
        ax2.set_xlabel('')
        ax3.set_xlabel('')
        
        ax1.get_xaxis().set_ticks([])
        ax2.get_xaxis().set_ticks([])
        ax3.get_xaxis().set_ticks([])
        
        # set title
        ax1.set_title('Rolling Returns', fontsize = 15)
        ax5.set_title('Distribution of Rolling Returns', fontsize = 15)        
    
        plt.show()
        
    else: 
        raise customExceptions.invalidInput('Invalid Horizon: Expect list of 4 window values')

def main():
    pass

if __name__ == "__main__":
    main()    
    