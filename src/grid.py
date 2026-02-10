"""
grid.py
Handles grid creation and initialization
"""

import numpy as np


class Grid:
    def __init__(self, width=50, height=50, randomize=True):
        self.width = width
        self.height = height

        if randomize:
            self.grid = np.random.randint(0, 2, (height, width))
        else:
            self.grid = np.zeros((height, width))

    def get_grid(self):
        return self.grid

    def set_cell(self, x, y, value):
        self.grid[y, x] = value

    def count_alive(self):
        return np.sum(self.grid)

    def reset_random(self):
        self.grid = np.random.randint(0, 2, (self.height, self.width))
