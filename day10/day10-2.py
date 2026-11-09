import sys

sys.setrecursionlimit(10000)


def press_buttons(state, buttons, counter, goal):
    state_str = str(state)
    for i in range(len(state)):
        if state[i] > goal[i]:
            return
    if state_str not in RECORDS:
        RECORDS[state_str] = counter
    elif counter >= RECORDS[state_str] or (
        str(goal) in RECORDS and RECORDS[str(goal)] < counter
    ):
        return
    RECORDS[state_str] = counter
    for button in buttons:
        new_state = state.copy()
        for idx in button:
            new_state[idx] += 1
        press_buttons(new_state, buttons, counter + 1, goal)


with open("day10_input.txt", "r") as file:
    data = file.read().split("\n")


total = 0
for idx, row in enumerate(data):
    print(idx)
    goal = [int(num) for num in row.split("{")[1][:-1].split(",")]
    buttons = [
        [int(num) for num in button.strip()[:-1].split(",")]
        for button in row.split("]")[1].split("{")[0].strip().split("(")[1:]
    ]

    RECORDS = {}
    press_buttons([0 for _ in range(len(goal))], buttons, 0, goal)
    print(RECORDS[str(goal)])
    total += RECORDS[str(goal)]
    print(len(RECORDS), "RECORDS len")
    with open("output.txt", "w") as file:
        for record in RECORDS:
            file.write(f"{record}, {RECORDS[record]}\n")
    exit()

print(total)
