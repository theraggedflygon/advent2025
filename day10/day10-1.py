import sys

sys.setrecursionlimit(10000)


def press_buttons(state, buttons, counter, goal_str):
    state_str = "".join(state)
    if state_str not in RECORDS:
        RECORDS[state_str] = counter
    elif counter >= RECORDS[state_str] or (
        goal_str in RECORDS and RECORDS[goal_str] < counter
    ):
        return
    RECORDS[state_str] = counter
    for button in buttons:
        new_state = state.copy()
        for idx in button:
            if new_state[idx] == "#":
                new_state[idx] = "."
            else:
                new_state[idx] = "#"
        press_buttons(new_state, buttons, counter + 1, goal_str)


with open("day10_input.txt", "r") as file:
    data = file.read().split("\n")


total = 0
for idx, row in enumerate(data):
    print(idx)
    goal = list(row[1:].split("]")[0])
    goal_str = "".join(goal)
    buttons = [
        [int(num) for num in button.strip()[:-1].split(",")]
        for button in row.split("]")[1].split("{")[0].strip().split("(")[1:]
    ]

    RECORDS = {}
    press_buttons(["." for _ in range(len(goal))], buttons, 0, goal_str)
    total += RECORDS[goal_str]

print(total)
