def calculate_pathways(row, col):
    if str([row, col]) in CACHE:
        return CACHE[str([row, col])]
    elif row + 1 == len(GRID):
        result =  1
    elif [row, col] in SPLITTERS:
        result = calculate_pathways(row, col - 1) + calculate_pathways(row, col + 1)
    else:
        result = calculate_pathways(row + 1, col)
    CACHE[str([row, col])] = result
    return result

with open("day7_input.txt", 'r') as file:
    GRID = file.read().split("\n")

start = None
SPLITTERS = []
for row in range(len(GRID)):
    for col in range(len(GRID[0])):
        if GRID[row][col] == 'S':
            start = [row, col]
        elif GRID[row][col] == "^":
            SPLITTERS.append([row, col])

CACHE = dict()
result = calculate_pathways(start[0], start[1])
print(result)
