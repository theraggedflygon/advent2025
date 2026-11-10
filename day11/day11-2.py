def traverse(node, end):
    if node in path_count:
        return path_count[node]

    count = 0
    if node == end:
        return 1

    for child in nodes[node]:
        count += traverse(child, end)

    path_count[node] = count
    return count


with open("day11_input.txt", "r") as file:
    data = file.read().split("\n")

nodes = {}

for row in data:
    key, children = row.split(":")
    children = children.strip().split(" ")
    nodes[key] = children

nodes["out"] = []

path_count = {}
svr2dac = traverse("svr", "dac")
path_count = {}
svr2fft = traverse("svr", "fft")
path_count = {}
dac2fft = traverse("dac", "fft")
path_count = {}
fft2dac = traverse("fft", "dac")
path_count = {}
fft2out = traverse("fft", "out")
path_count = {}
dac2out = traverse("dac", "out")

print(svr2dac * dac2fft * fft2out + svr2fft * fft2dac * dac2out)
