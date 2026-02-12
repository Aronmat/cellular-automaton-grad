import numpy as np


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols), dtype=int)

    def randomize(self, density=0.3):
        """
        Fill grid randomly based on density.
        density = probability a cell is alive.
        """
        self.grid = np.random.choice(
            [0, 1],
            size=(self.rows, self.cols),
            p=[1 - density, density]
        )

    def get_neighbors(self, row, col):
        """
        Count live neighbors (8-neighborhood).
        Cells outside grid are dead.
        """
        total = 0

        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):

                if (i == row and j == col):
                    continue

                if 0 <= i < self.rows and 0 <= j < self.cols:
                    total += self.grid[i, j]

        return total

    def copy(self):
        new_grid = Grid(self.rows, self.cols)
        new_grid.grid = self.grid.copy()
        return new_grid

    # ✅ ADD THIS
    def get_grid(self):
        return self.grid
    
    def count_alive(self):
        """
        Count total live cells in the grid.
        """
        return np.sum(self.grid)