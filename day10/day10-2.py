from scipy.optimize import linprog

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
    button_matrix = []
    for light in range(len(goal)):
        button_row = []
        for button in buttons:
            if light in button:
                button_row.append(1)
            else:
                button_row.append(0)
        button_matrix.append(button_row)

    c = [1 for _ in range(len(buttons))]

    result = linprog(c, A_eq=button_matrix, b_eq=goal, integrality=c)
    total += int(result.fun)

print(total)

# A = [[0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 1], [0, 0, 1, 1, 1, 0], [1, 1, 0, 1, 0, 0]]
# b = [3, 5, 4, 7]

# c = [1, 1, 1, 1, 1, 1]

# result = linprog(c, A_eq=A, b_eq=b)
# print(result.fun)
