# -*- coding: utf-8 -*-


import unittest
import portfolioFactory
import portfolioFactory.portfolio.test_portfolio as test_portfolio
from portfolioFactory.portfolio import portfolio as portfolio
from portfolioFactory.utils.customExceptions import *


## Test to validate both inputs must be a list
class testListInput(unittest.TestCase):
    def setUp(self):
        self.itema = 55
        self.itemb = 77
    def test_interior(self):
        self.assertRaises(notListError,portfolio.portfolio(self.itema,self.itemb))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(test_portfolio)
    unittest.TextTestRunner(verbosity=2).run(suite)

