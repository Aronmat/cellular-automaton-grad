import matplotlib.pyplot as plt
import numpy as np


class Visualizer:
    def __init__(self, automaton):
        self.automaton = automaton
        self.fig, self.ax = plt.subplots()
        self.img = self.ax.imshow(
            self.automaton.get_grid(),
            cmap="binary"
        )

        # Connect mouse click event
        self.fig.canvas.mpl_connect(
            "button_press_event",
            self.on_click
        )

    def on_click(self, event):
        """
        Toggle cell state when user clicks grid.
        """
        if event.inaxes != self.ax:
            return

        col = int(event.xdata)
        row = int(event.ydata)

        grid = self.automaton.grid.grid

        # Toggle cell
        grid[row, col] = 1 - grid[row, col]

        self.update_display()

    def update_display(self):
        self.img.set_data(self.automaton.get_grid())
        plt.draw()

    def run(self):
        plt.show()
