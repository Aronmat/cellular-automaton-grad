import numpy as np

from src.automaton import CellularAutomaton

# Create automaton
ca = CellularAutomaton(10, 10)

# Randomize grid
ca.randomize(0.3)

print("Initial Grid:\n")
print(ca.get_grid())

print("\nRunning Simulation...\n")

# Run 5 generations
ca.run(5)  # make sure run() is added to automaton.py

print("\nFinal Grid:\n")
print(ca.get_grid())

print("\nFinal Alive Cells:", ca.count_alive())

# Grid Test
from src.grid import Grid

grid = Grid(10, 10)
grid.randomize(0.3)  # you can randomize it too

print("\nGrid Test:\n")
print(grid.grid)  # get_grid() no longer needed if we use 'grid.grid'

# Count alive cells for raw grid
print("Alive cells:", np.sum(grid.grid))
