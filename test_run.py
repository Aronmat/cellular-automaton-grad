from src.automaton import CellularAutomaton

ca = CellularAutomaton(10, 10)

ca.randomize(0.3)

print("Initial Grid:\n")
print(ca.get_grid())

print("\nRunning Simulation...\n")

ca.run(5)

print("\nFinal Alive Cells:", ca.count_alive())

# Grid Test
from src.grid import Grid

grid = Grid(10, 10)

print(grid.get_grid())
print("Alive cells:", grid.count_alive())
# Rules Test
from src.rules import Rules

print("\nNext Generation:\n")

next_grid = Rules.apply_rules(grid.get_grid())
print(next_grid)
