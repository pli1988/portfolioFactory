# -*- coding: utf-8 -*-

import riskMetrics
import unittest

class TestRiskMetricsFunctions(unittest.TestCase):

    def setUp(self):
        self.data = range(10)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRiskMetricsFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)