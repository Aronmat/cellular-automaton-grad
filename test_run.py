import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from src.automaton import CellularAutomaton
import os
import json

ROWS, COLS = 30, 30


# ========================
# RULE INPUT FUNCTION
# ========================
def get_rule_input(prompt):
    while True:
        user_input = input(prompt).strip()

        if not user_input:
            print("Input cannot be empty. Please enter numbers between 0 and 8.")
            continue

        try:
            numbers = []
            for part in user_input.split(","):
                part = part.strip()

                if not part.isdigit():
                    raise ValueError("Only integers allowed.")

                value = int(part)

                if not 0 <= value <= 8:
                    raise ValueError("Values must be between 0 and 8.")

                numbers.append(value)

            return sorted(set(numbers))

        except ValueError as e:
            print(f"Invalid input: {e}")
            print("Example format: 2,3")


# ========================
# MAIN PROGRAM
# ========================
def main():

    # ---- CUSTOM RULES ----
    while True:
        custom_rules = input("Do you want to use custom rules? (y/n): ").strip().lower()
        if custom_rules in ["y", "n"]:
            break
        print("Invalid input. Please enter 'y' or 'n'.")

    if custom_rules == "y":
        survival_rules = get_rule_input(
            "Enter survival counts for a live cell (comma-separated, e.g., 2,3): "
        )
        birth_rules = get_rule_input(
            "Enter birth counts for a dead cell (comma-separated, e.g., 3): "
        )

        print("Using custom rules:")
        print("Survival:", survival_rules)
        print("Birth:", birth_rules)

        rules_file = "temp_rules.json"
        with open(rules_file, "w") as f:
            json.dump({"survival": survival_rules, "birth": birth_rules}, f)
    else:
        rules_file = "rules.json"

    # ---- PREDEFINED STATES ----
    predefined_states = {
        "glider": [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)],
        "block": [(10, 10), (10, 11), (11, 10), (11, 11)],
        "blinker": [(15, 14), (15, 15), (15, 16)]
    }

    # ---- INIT AUTOMATON ----
    ca = CellularAutomaton(ROWS, COLS, rules_file=rules_file)

    print("Choose initial state mode:")
    print("1 - Predefined states")
    print("2 - Custom state")
    print("3 - Random state")
    print("4 - Load saved state")

    while True:
        mode = input("Enter 1, 2, 3, or 4: ").strip()
        if mode in ["1", "2", "3", "4"]:
            break
        print("Invalid selection.")

    if mode == "1":
        print("Available predefined states:")
        for key in predefined_states:
            print("-", key)

        choice = input("Enter your choice: ").strip().lower()
        ca.grid.randomize(0.0)

        if choice in predefined_states:
            for row, col in predefined_states[choice]:
                ca.grid.grid[row, col] = 1
        else:
            print("Unknown choice, starting random.")
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
                    print("Coordinates out of range.")
            except:
                print("Invalid format. Use row,col")

    elif mode == "3":
        ca.randomize(0.3)

    elif mode == "4":
        filename = input("Enter filename to load: ").strip()
        try:
            ca.load_state(filename)
        except Exception as e:
            print("Failed to load state:", e)
            ca.randomize(0.3)

    # ---- PLOT ----
    fig, ax = plt.subplots()
    img = ax.imshow(ca.get_grid(), cmap="Greys")
    plt.title("Cellular Automaton | SPACE: Pause | S: Save | Click: Toggle Cell")

    paused = False

    def update(frame):
        nonlocal paused
        if not paused:
            ca.step()
            img.set_data(ca.get_grid())
        return [img]

    def on_key(event):
        nonlocal paused
        if event.key == " ":
            paused = not paused
            print("Paused" if paused else "Resumed")
        elif event.key.lower() == "s":
            os.makedirs("states", exist_ok=True)
            filename = input("Enter filename to save (without extension): ").strip()
            filename = os.path.join("states", filename + ".npy")
            ca.save_state(filename)
            print("Saved to", filename)

    def on_click(event):
        if event.inaxes != ax:
            return
        row = int(event.ydata)
        col = int(event.xdata)
        if 0 <= row < ROWS and 0 <= col < COLS:
            ca.grid.grid[row, col] ^= 1
            img.set_data(ca.get_grid())
            plt.draw()

    fig.canvas.mpl_connect("key_press_event", on_key)
    fig.canvas.mpl_connect("button_press_event", on_click)

    ani = FuncAnimation(fig, update, interval=200, cache_frame_data=False)

    print("\nControls:")
    print("------------------------------------------------")   
    print("SPACE  - Pause / Resume simulation")
    print("S      - Save current state")
    print("Click  - Toggle individual cell")
    print("Close window to return to menu")
    print("------------------------------------------------\n")
    
    plt.show()


# ========================
# PROGRAM LOOP
# ========================
while True:
    main()

    print("\nWhat would you like to do?")
    print("1 - Restart program")
    print("2 - Exit")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "2":
        print("Exiting program...")
        break