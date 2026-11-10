def traverse(node):
    count = 0
    if node == "out":
        return 1

    for child in nodes[node]:
        count += traverse(child)

    return count


with open("day11_input.txt", "r") as file:
    data = file.read().split("\n")

nodes = {}

for row in data:
    key, children = row.split(":")
    children = children.strip().split(" ")
    nodes[key] = children

result = traverse("you")
print(result)
