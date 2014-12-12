from ..utils import utils as utils
from ..utils import customExceptions as customExceptions


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import portfolioFactory.metrics.riskMetrics as riskMetrics



def plotWithStats(series,startyear,endyear):
    ''' Function to plot cumulative returns including risk metrics as text
        The plot and risk metrics are calculated between startyear-endyear
        
        Arguments:
        -series (series) : a series containing returns
        -staryear(integer): year to begin the plot and analysis
        -endyear (integer): year to end the plot and analysis
    
        Result:
        Shows a matplotlib figure containing cumulative returns and the risk metrics
        
    '''
    
    #limit to years of interest
    try:
        measure = series.truncate(before='01/01/'+str(startyear),after='12/31/'+str(endyear))
        
    except (TypeError, ValueError) as e:
        raise customExceptions.invalidInput('Invalid year specified')
        
    if len(measure)==0:
        raise customExceptions.invalidInput("The series passed does not contain data in the specified interval")
    
    #calculate cumulative returns
    cumulative =  (measure+1).cumprod()
    
    # calculate risk metrics
    metric1 = round(riskMetrics.VaR(measure,12,95),2)
    metric2 = round(riskMetrics.maxDrawdown(measure),2)
    
    
    #plot 
    current_palette = sns.color_palette("Blues")
    text_date = '01/01/'+str(startyear+1)
    text_y = 0.95*(cumulative.max()-cumulative.min())
    
    cumulative.plot()
    plt.xlabel('Date')
    plt.ylabel('Total Value')
    plt.title('Cumulative Returns')
    plt.text(text_date, text_y, 'VaR='+str(metric1)+', Max Draw='+str(metric2),fontsize=15)
    plt.grid(True)
    plt.show()
    
    
    
def main():
    pass

if __name__ == "__main__":
    main() 
