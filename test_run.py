import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from src.automaton import CellularAutomaton
import os

# --- Predefined starting states ---
predefined_states = {
    "glider": [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)],
    "block": [(10, 10), (10, 11), (11, 10), (11, 11)],
    "blinker": [(15, 14), (15, 15), (15, 16)]
}

# --- Initialize automaton ---
ca = CellularAutomaton(30, 30)

# --- User menu ---
print("Choose initial state mode:")
print("1 - Predefined states (glider, block, blinker)")
print("2 - Custom state")
print("3 - Random state")
print("4 - Load saved state")
mode = input("Enter 1, 2, 3, or 4: ").strip()

if mode == "1":
    print("Available predefined states:")
    for key in predefined_states.keys():
        print("-", key)
    choice = input("Enter your choice: ").strip().lower()
    ca.grid.randomize(0.0)  # start empty
    if choice in predefined_states:
        for row, col in predefined_states[choice]:
            ca.grid.grid[row, col] = 1
    else:
        print("Unknown choice, starting random state.")
        ca.randomize(0.3)

elif mode == "2":
    ca.grid.randomize(0.0)  # start empty
    print("Enter live cell coordinates as row,col (0-29). Type 'done' to finish.")
    while True:
        entry = input("Cell coordinate: ").strip()
        if entry.lower() == "done":
            break
        try:
            row, col = map(int, entry.split(","))
            if 0 <= row < 30 and 0 <= col < 30:
                ca.grid.grid[row, col] = 1
            else:
                print("Coordinates out of range (0-29).")
        except:
            print("Invalid format. Use row,col")

elif mode == "3":
    ca.randomize(0.3)

elif mode == "4":
    filename = input("Enter filename to load (e.g., states/my_state.npy): ").strip()
    try:
        ca.load_state(filename)
    except Exception as e:
        print("Failed to load state:", e)
        ca.randomize(0.3)

else:
    print("Unknown mode. Starting random state.")
    ca.randomize(0.3)

# --- Plot setup ---
fig, ax = plt.subplots()
img = ax.imshow(ca.get_grid(), cmap="Greys")
plt.title("Cellular Automaton")

paused = False

# --- Animation update ---
def update(frame):
    global paused
    if not paused:
        ca.step()
        img.set_data(ca.get_grid())
    return [img]

# --- Pause / Resume and Save on key press ---
def on_key(event):
    global paused
    if event.key == " ":
        paused = not paused
        print("Paused" if paused else "Resumed")
    elif event.key.lower() == "s":
        os.makedirs("states", exist_ok=True)
        filename = input("Enter filename to save state (e.g., states/my_state.npy): ").strip()
        ca.save_state(filename)
        print(f"State saved to {filename}")

fig.canvas.mpl_connect("key_press_event", on_key)

# --- Run animation ---
ani = FuncAnimation(fig, update, frames=200, interval=200)
plt.show()
