import numpy as np
from src.grid import Grid


class CellularAutomaton:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = Grid(rows, cols)

    def randomize(self, density=0.3):
        """
        Randomly initialize the grid.
        """
        self.grid.randomize(density)

    def step(self):
        """
        Advance simulation by one generation
        using Conway's Game of Life rules.
        """
        new_grid = self.grid.copy()

        for i in range(self.rows):
            for j in range(self.cols):

                neighbors = self.grid.get_neighbors(i, j)
                cell = self.grid.grid[i, j]

                # Game of Life rules
                if cell == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid.grid[i, j] = 0
                else:
                    if neighbors == 3:
                        new_grid.grid[i, j] = 1

        self.grid = new_grid

    def run(self, steps):
        """
        Run the simulation for multiple generations.
        """
        for _ in range(steps):
            self.step()

    def get_grid(self):
        """
        Return current grid state.
        """
        return self.grid.grid   # <-- FIXED

    def count_alive(self):
        """
        Count total live cells.
        """
        return np.sum(self.grid.grid)
    def run(self, generations):
        """
        Run the automaton for a number of generations.
        """
        for _ in range(generations):
            self.step()