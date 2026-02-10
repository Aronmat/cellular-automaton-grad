import numpy as np


class CellularAutomaton:
    def __init__(self, rows=50, cols=50):
        """
        Initialize grid and simulation parameters.
        """
        self.rows = rows
        self.cols = cols

        # 0 = dead, 1 = alive
        self.grid = np.zeros((rows, cols), dtype=int)

    def randomize(self, density=0.2):
        """
        Random initial state.
        """
        self.grid = np.random.choice(
            [0, 1],
            size=(self.rows, self.cols),
            p=[1 - density, density]
        )

    def get_grid(self):
        return self.grid
