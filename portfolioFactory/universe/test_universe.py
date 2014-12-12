"""
test_universe contains the unit tests for the universe class

To run all test, go to the the main ./portfolioFactory directory and run

>> python -m unittest discover

Author: Peter Li

"""

import unittest

import portfolioFactory.universe.universe as universe
from ..utils import customExceptions as customExceptions

class TestUniverse(unittest.TestCase):
    '''Test cases for universe'''

    def setUp(self):
        # File paths
        self.validPath = './portfolioFactory/universe/totalReturnData'
        self.invalidPath = './portfolioFactory/universe/universe.py'
        self.name = 'testName'
        
        
##############################################################################
# Test init
##############################################################################

    def testuniverse_inputNotPickle(self):
        # retun file path is not a pickle
         
        self.assertRaises(customExceptions.badData, universe.universe,self.name, self.invalidPath)
        
    def testuniverse_inputNotFile(self):
        # return file is not a file
         
        self.assertRaises(customExceptions.badData, universe.universe,self.name, 2)
        
    def testuniverse_badName(self):
        # invlaid name
         
        self.assertRaises(customExceptions.badData, universe.universe, ['abc'], self.validPath)
 
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUniverse)
    unittest.TextTestRunner(verbosity=2).run(suite)