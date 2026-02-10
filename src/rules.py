import numpy as np


class Rules:
    """
    Handles automaton rule logic (Conway's Game of Life by default).
    """

    @staticmethod
    def count_neighbors(grid, x, y):
        """
        Count alive neighbors around a cell.
        Uses Moore neighborhood (8 neighbors).
        """

        rows, cols = grid.shape
        total = 0

        for i in range(-1, 2):
            for j in range(-1, 2):

                if i == 0 and j == 0:
                    continue  # Skip the cell itself

                nx = (x + i) % rows
                ny = (y + j) % cols

                total += grid[nx, ny]

        return total

    @staticmethod
    def apply_rules(grid):
        """
        Apply Conway's Game of Life rules to entire grid.
        """

        rows, cols = grid.shape
        new_grid = np.copy(grid)

        for x in range(rows):
            for y in range(cols):

                neighbors = Rules.count_neighbors(grid, x, y)

                # Rule 1: Underpopulation
                if grid[x, y] == 1 and neighbors < 2:
                    new_grid[x, y] = 0

                # Rule 2: Overpopulation
                elif grid[x, y] == 1 and neighbors > 3:
                    new_grid[x, y] = 0

                # Rule 3: Reproduction
                elif grid[x, y] == 0 and neighbors == 3:
                    new_grid[x, y] = 1

                # Rule 4: Survival → stays same otherwise

        return new_grid
