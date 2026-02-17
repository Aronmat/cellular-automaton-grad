import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from src.automaton import CellularAutomaton

# =========================
# Create automaton
# =========================
ca = CellularAutomaton(30, 30)
ca.randomize(0.3)

# =========================
# Plot setup
# =========================
fig, ax = plt.subplots()

img = ax.imshow(ca.get_grid(), cmap="Greys")

paused = False

# =========================
# Animation update
# =========================
def update(frame):
    global paused

    if not paused:
        ca.step()
        img.set_data(ca.get_grid())

    return [img]

# =========================
# Pause / Resume (SPACEBAR)
# =========================
def on_key(event):
    global paused

    if event.key == " ":
        paused = not paused
        print("Paused" if paused else "Resumed")

# =========================
# CLICK TO TOGGLE CELLS
# (Graduate Requirement)
# =========================
def on_click(event):
    if event.inaxes != ax:
        return

    col = int(event.xdata)
    row = int(event.ydata)

    grid = ca.grid.grid

    # Toggle cell state
    grid[row, col] = 1 - grid[row, col]

    img.set_data(grid)
    plt.draw()

# =========================
# Event bindings
# =========================
fig.canvas.mpl_connect("key_press_event", on_key)
fig.canvas.mpl_connect("button_press_event", on_click)

# =========================
# Run animation
# =========================
ani = FuncAnimation(fig, update, interval=200)

plt.title("Interactive Cellular Automaton")
plt.show()
