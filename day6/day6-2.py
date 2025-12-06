with open("day6_input.txt", 'r') as file:
    rows = file.read().split("\n")

total = 0
term = 0
operation = ""
for i in range(len(rows[0])):
    num_str = ""
    for row in rows[:-1]:
        if row[i] != " ":
            num_str += row[i]
    
    if rows[-1][i] == "*":
        term = 1
        operation = "*"

    elif rows[-1][i] == "+":
        term = 0
        operation = "+"

    if num_str == "":
        total += term
    elif operation == "*":
        term *= int(num_str)
    else:
        term += int(num_str)

total += term
print(total)