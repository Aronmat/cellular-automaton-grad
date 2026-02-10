from src.automaton import CellularAutomaton

ca = CellularAutomaton(10, 10)
ca.randomize(0.3)

print("Initial Grid:\n")
print(ca.get_grid())
