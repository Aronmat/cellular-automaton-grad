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
    def set_initial_state(self, live_cells):
        """
        live_cells: list of (row, col) tuples to set as alive
        """
        # Reset grid first
        self.grid.grid[:] = 0
        for row, col in live_cells:
            if 0 <= row < self.rows and 0 <= col < self.cols:
                self.grid.grid[row, col] = 1
            
       # --- New Methods ---
    def save_state(self, filename):
        """Save the current grid to a .npy file."""
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        np.save(filename, self.grid.grid)
        print(f"Grid saved to {filename}")

    def load_state(self, filename):
        """Load a grid from a .npy file."""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found.")
        
        loaded_grid = np.load(filename)

        if loaded_grid.shape != (self.rows, self.cols):
            raise ValueError(
                f"State shape {loaded_grid.shape} does not match automaton size ({self.rows}, {self.cols})"
            )

        self.grid.grid = loaded_grid
        print(f"Grid loaded from {filename}")
        
    def save_state(self, filename):
        # Ensure .npy
        if not filename.endswith(".npy"):
            filename += ".npy"

        # Default folder
        folder = os.path.dirname(filename)
        if folder == "":
            folder = "states"
            filename = os.path.join(folder, filename)

        os.makedirs(folder, exist_ok=True)
        np.save(filename, self.grid.grid)
        print(f"Saved state to {filename}")

    def load_state(self, filename):
        data = np.load(filename)
        if data.shape != (self.rows, self.cols):
            raise ValueError(
                f"State shape {data.shape} does not match automaton size ({self.rows}, {self.cols})"
            )
        self.grid.grid = data.copy()
        print(f"Loaded state from {filename}")