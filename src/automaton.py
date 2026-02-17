import numpy as np
import json
from src.grid import Grid


class CellularAutomaton:
    def __init__(self, rows, cols, rules_file="rules.json"):
        self.rows = rows
        self.cols = cols
        self.grid = Grid(rows, cols)

        # Load rules
        with open(rules_file, "r") as f:
            rules = json.load(f)

        self.survival_rules = rules["survival"]
        self.birth_rules = rules["birth"]

    def randomize(self, density=0.3):
        self.grid.randomize(density)

    def step(self):
        new_grid = self.grid.copy()

        for i in range(self.rows):
            for j in range(self.cols):

                neighbors = self.grid.get_neighbors(i, j)
                cell = self.grid.grid[i, j]

                if cell == 1:
                    if neighbors not in self.survival_rules:
                        new_grid.grid[i, j] = 0
                else:
                    if neighbors in self.birth_rules:
                        new_grid.grid[i, j] = 1

        self.grid = new_grid

    def run(self, steps=1):
        for _ in range(steps):
            self.step()

    def get_grid(self):
        return self.grid.grid

    def count_alive(self):
        return np.sum(self.grid.grid)
