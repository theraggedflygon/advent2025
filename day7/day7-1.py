with open("day7_input.txt", 'r') as file:
    grid = file.read().split("\n")

beams = []
splitters = []
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 'S':
            beams.append([row, col])
        elif grid[row][col] == "^":
            splitters.append([row, col])

hit_splitters = []
while len(beams) > 0:
    new_beams = []
    for beam in beams:
        if beam[0] + 1 == len(grid):
            continue
        elif [beam[0] + 1,beam[1]] in splitters:
            if [beam[0] + 1, beam[1]] not in hit_splitters:
                hit_splitters.append([beam[0] + 1, beam[1]])
            if [beam[0], beam[1] - 1] not in new_beams:
                new_beams.append([beam[0], beam[1] - 1])
            if [beam[0], beam[1] + 1] not in new_beams:
                new_beams.append([beam[0], beam[1] + 1])
        else:
            new_beams.append([beam[0] + 1, beam[1]])
    beams = new_beams

print(len(hit_splitters))
