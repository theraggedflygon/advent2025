with open("day1_input.txt", 'r') as file:
    moves = file.read().split("\n")

WHEEL_LENGTH = 100

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

    full = jump // WHEEL_LENGTH
    count += full
    remainder = jump % WHEEL_LENGTH

    if position != 0 and (position + (modifier * remainder) <= 0 or position + (modifier * remainder) >= WHEEL_LENGTH):
        count += 1

    position = (position + (modifier * jump)) % WHEEL_LENGTH


print(count)
