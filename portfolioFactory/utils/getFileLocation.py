# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 17:15:15 2014

@author: peter
"""

import Tkinter,tkFileDialog

def getFileLocation():
    
    root = Tkinter.Tk()
    root.withdraw()
    
    filePath = tkFileDialog.askopenfilename(initialdir="./",title = 'Please select the returns file')   
    
    return filePath