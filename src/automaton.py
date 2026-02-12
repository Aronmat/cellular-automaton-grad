import numpy as np
from src.grid import Grid
from src.rules import Rules


class CellularAutomaton:
    """
    Main simulation controller.
    """

    def __init__(self, rows, cols):
        self.grid = Grid(rows, cols)

    def randomize(self, density=0.3):
        """
        Randomly populate grid.
        """
        self.grid.randomize(density)

    def step(self):
        """
        Advance one generation.
        """
        current = self.grid.get_grid()
        new_state = Rules.apply_rules(current)
        self.grid.set_grid(new_state)

    def run(self, steps=10):
        """
        Run simulation for N steps.
        """
        for i in range(steps):
            print(f"\nGeneration {i+1}:\n")
            self.step()
            print(self.grid.get_grid())

    def get_grid(self):
        return self.grid.get_grid()

    def count_alive(self):
        return np.sum(self.grid.get_grid())
