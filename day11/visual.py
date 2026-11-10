import matplotlib.pyplot as plt
import networkx as nx

with open("day11_input.txt", "r") as file:
    data = file.read().split("\n")

nodes = {}

for row in data:
    key, children = row.split(":")
    children = children.strip().split(" ")
    nodes[key] = children

G = nx.DiGraph()

node_colors = ["green"]

G.add_node("out")

for key in nodes:
    G.add_node(key)
    if key == "svr":
        node_colors.append("skyblue")
    elif key == "dac" or key == "fft":
        node_colors.append("red")
    else:
        node_colors.append("black")

for key in nodes:
    for child in nodes[key]:
        G.add_edge(key, child)


nx.draw(
    G,
    nx.circular_layout(G),
    with_labels=True,
    node_color=node_colors,
    node_size=10,
    width=1,
)
plt.show()
