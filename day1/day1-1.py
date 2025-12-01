with open("day1_input.txt", 'r') as file:
    moves = file.read().split("\n")

position = 50
modifier = 1
count = 0
for move in moves:
    direction = move[0]
    jump = int(move[1:])
    
    if direction == 'L':
        modifier = -1
    else:
        modifier = 1
    
    position = (position + (modifier * jump)) % 100
    if position == 0:
        count += 1

print(count)
