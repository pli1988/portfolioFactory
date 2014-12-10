# -*- coding: utf-8 -*-
"""
@author: Israel
"""

''' Module to preform unit tests on strategy class

'''
    
import pandas as pd
import numpy as np
import datetime
import portfolioFactory
from ..universe import universe as universe
from ..exceptions.exceptions import *
    

class TestmergeIntervals(unittest.TestCase):
    def setUp(self):
        self.itema = interval("[5,10]")
	   self.itemb = interval("(5,10)")
        self.mymerge = mergeIntervals(self.itema,self.itemb)
    def test_interior(self):
        self.assertEqual(self.mymerge.leftreal, self.itema.leftreal)

if __name__ == '__main__':
    unittest.main()