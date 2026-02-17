import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from src.automaton import CellularAutomaton

# Create automaton
ca = CellularAutomaton(30, 30)
ca.randomize(0.3)

# Plot setup
fig, ax = plt.subplots()
img = ax.imshow(ca.get_grid(), cmap="Greys")

paused = False


# Animation update
def update(frame):
    global paused

    if not paused:
        ca.step()
        img.set_data(ca.get_grid())

    return [img]


# Pause / Resume
def on_key(event):
    global paused

    if event.key == " ":
        paused = not paused
        print("Paused" if paused else "Resumed")


# CLICK TO TOGGLE CELL (GRAD FEATURE)
def on_click(event):
    if event.inaxes != ax:
        return

    x = int(event.ydata)
    y = int(event.xdata)

    grid = ca.grid.grid

    # Toggle cell
    grid[x, y] = 0 if grid[x, y] == 1 else 1

    img.set_data(grid)
    plt.draw()


# Event bindings
fig.canvas.mpl_connect("key_press_event", on_key)
fig.canvas.mpl_connect("button_press_event", on_click)

# Animation
ani = FuncAnimation(fig, update, frames=200, interval=200)

plt.title("Interactive Cellular Automaton")
plt.show()
