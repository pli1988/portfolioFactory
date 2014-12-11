# -*- coding: utf-8 -*-


import unittest
from  portfolioFactory.portfolio import test_portfolio as test_portfolio
from portfolioFactory.portfolio import portfolio as portfolio
import portfolioFactory.utils.customExceptions as customExceptions


## Test to validate both inputs must be a list
class testListInput(unittest.TestCase):
    def setUp(self):
        self.itema = 55
        self.itemb = 77
    def test_interior(self):
        pass
        # self.assertRaises(Exception,portfolio.portfolio(self.itema,self.itemb))
        
## Test to validate both inputs must be a list
class testListInput(unittest.TestCase):
    def setUp(self):
        self.itema = [55,55]
        self.itemb = [77]
        print self.itema
    def test_interior(self):
        self.assertRaises(Exception,portfolio.portfolio(self.itema,self.itemb))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(test_portfolio)
    unittest.TextTestRunner(verbosity=2).run(suite)

