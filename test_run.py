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


def update(frame):
    global paused

    if not paused:
        ca.step()
        img.set_data(ca.get_grid())

    return [img]


def on_key(event):
    global paused

    if event.key == " ":
        paused = not paused
        print("Paused" if paused else "Resumed")


fig.canvas.mpl_connect("key_press_event", on_key)

ani = FuncAnimation(fig, update, frames=200, interval=200)

plt.title("Cellular Automaton")
plt.show()

