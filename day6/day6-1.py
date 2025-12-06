with open("day6_input.txt", 'r') as file:
    rows = [row.split() for row in file.read().split("\n")]

total = 0

for i in range(len(rows[0])):
    if rows[-1][i] == "*":
        term = 1
        for row in rows[:-1]:
            term *= int(row[i])
    else:
        term = 0
        for row in rows[:-1]:
            term += int(row[i])
    
    total += term

print(total)