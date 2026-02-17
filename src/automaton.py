import numpy as np
import json
from src.grid import Grid
import os


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
    
    def load_state(self, file_path, position="center"):
        """
        Load a saved grid state from a .npy file.
        Small states can be embedded into the larger grid.
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"State file not found: {file_path}")

        data = np.load(file_path)

        # Create empty grid
        new_grid = np.zeros((self.rows, self.cols), dtype=int)

        state_rows, state_cols = data.shape

        if state_rows > self.rows or state_cols > self.cols:
            raise ValueError("State is larger than automaton grid.")

        # Placement logic
        if position == "center":
            start_row = (self.rows - state_rows) // 2
            start_col = (self.cols - state_cols) // 2
        else:
            start_row, start_col = position  # tuple (row, col)

        # Insert state
        new_grid[
            start_row:start_row + state_rows,
            start_col:start_col + state_cols
        ] = data

        self.grid.grid = new_grid
