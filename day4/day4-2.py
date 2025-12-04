with open("day4_input.txt", 'r') as file:
    grid = [list(row) for row in file.read().split("\n")]


height = len(grid)
width = len(grid[0])
adj = [[0 for _ in range(width)] for _ in range(height)]
offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(height):
    for j in range(width):
        if grid[i][j] != '@':
            continue
        for row_delta, col_delta in offsets:
            if 0 <= i + row_delta < height and 0 <= j + col_delta < width:
                adj[i + row_delta][j + col_delta] += 1

total = 0
old_total = -1
while old_total != total:
    old_total = total
    for i in range(height):
        for j in range(width):
            if grid[i][j] == '@' and adj[i][j] < 4:
                total += 1
                grid[i][j] = "x"
                for row_delta, col_delta in offsets:
                    if 0 <= i + row_delta < height and 0 <= j + col_delta < width:
                        adj[i + row_delta][j + col_delta] -= 1

print(total)
