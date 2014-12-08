"""
EXAMPLE: Working with the uiverse class
"""

from universe import universe

# Create Instance of universe for US Equities
usEqUniverse = universe('usEquityConfig.txt')

# Get Summary Statistics
usEqUniverse.computeSummary()

# Plot Return
usEqUniverse.assetReturns.A.plot()