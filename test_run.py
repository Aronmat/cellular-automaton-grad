import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from src.automaton import CellularAutomaton
import os
import json

ROWS, COLS = 30, 30

# --- Custom rules option ---
print("Do you want to use custom rules? (y/n)")
custom_rules = input().strip().lower()

if custom_rules == "y":
    try:
        survival_input = input("Enter survival counts for a live cell (comma-separated, e.g., 2,3): ")
        birth_input = input("Enter birth counts for a dead cell (comma-separated, e.g., 3): ")

        survival_rules = [int(x) for x in survival_input.split(",") if x.strip().isdigit()]
        birth_rules = [int(x) for x in birth_input.split(",") if x.strip().isdigit()]

        # Save to temporary JSON for the automaton to load
        temp_rules_file = "temp_rules.json"
        with open(temp_rules_file, "w") as f:
            json.dump({"survival": survival_rules, "birth": birth_rules}, f)

        rules_file = temp_rules_file
        print(f"Using custom rules: survival={survival_rules}, birth={birth_rules}")
    except Exception as e:
        print("Invalid input. Using default rules.")
        rules_file = "rules.json"
else:
    rules_file = "rules.json"

# --- Predefined starting states ---
predefined_states = {
    "glider": [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)],
    "block": [(10, 10), (10, 11), (11, 10), (11, 11)],
    "blinker": [(15, 14), (15, 15), (15, 16)]
}

# --- Initialize automaton ---
ca = CellularAutomaton(ROWS, COLS, rules_file=rules_file)

# --- Initial state menu ---
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
        print("Unknown choice, starting with random state.")
        ca.randomize(0.3)

elif mode == "2":
    ca.grid.randomize(0.0)
    print("Enter live cell coordinates as row,col (0-29). Type 'done' to finish.")
    while True:
        entry = input("Cell coordinate: ").strip()
        if entry.lower() == "done":
            break
        try:
            row, col = map(int, entry.split(","))
            if 0 <= row < ROWS and 0 <= col < COLS:
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

# --- Pause / Resume and Save ---
def on_key(event):
    global paused
    if event.key == " ":
        paused = not paused
        print("Paused" if paused else "Resumed")
    elif event.key.lower() == "s":
        os.makedirs("states", exist_ok=True)
        filename = input("Enter filename to save state (without extension, saved in states/): ").strip()
        if not filename.endswith(".npy"):
            filename += ".npy"
        filename = os.path.join("states", filename)
        ca.save_state(filename)
        print(f"State saved to {filename}")

fig.canvas.mpl_connect("key_press_event", on_key)

# --- Click to toggle cells ---
def on_click(event):
    if event.inaxes != ax:
        return
    # Convert mouse position to grid coordinates
    row = int(event.ydata)
    col = int(event.xdata)
    if 0 <= row < ROWS and 0 <= col < COLS:
        # Toggle cell
        ca.grid.grid[row, col] = 0 if ca.grid.grid[row, col] == 1 else 1
        img.set_data(ca.get_grid())
        plt.draw()

# Bind click event
fig.canvas.mpl_connect("button_press_event", on_click)

# --- Run animation ---
ani = FuncAnimation(fig, update, frames=200, interval=200)
plt.show()
