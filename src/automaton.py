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

    def count_neighbors(self, row, col):
        """
        Count live neighbors using Moore neighborhood.
        """

        total = 0

        for i in range(-1, 2):
            for j in range(-1, 2):

                if i == 0 and j == 0:
                    continue

                r = row + i
                c = col + j

                if 0 <= r < self.rows and 0 <= c < self.cols:
                    total += self.grid[r, c]

        return total
    def step(self):
        """
        Advance automaton by one time step
        using Conway's Game of Life rules.
        """

        new_grid = np.copy(self.grid)

        for r in range(self.rows):
            for c in range(self.cols):

                neighbors = self.count_neighbors(r, c)

                # Rule 1 & 3: Death
                if self.grid[r, c] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[r, c] = 0

                # Rule 2: Birth
                else:
                    if neighbors == 3:
                        new_grid[r, c] = 1

        self.grid = new_grid
