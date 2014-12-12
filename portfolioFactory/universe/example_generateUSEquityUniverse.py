"""
EXAMPLE: Working with the uiverse class
"""

from universe import universe
import pandas as pd

# Create Instance of universe for US Equities
usEqUniverse = universe('usEquityConfig.txt')

# Get Summary Statistics
usEqUniverse.computeSummary()

# Plot Return
usEqUniverse.assetReturns.AA.plot()