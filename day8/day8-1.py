import bisect

PAIRS = 10

with open("day8_input.txt", 'r') as file:
    coord_data = file.read().split("\n")

boxes = []
for row in coord_data:
    coord = [int(num) for num in row.split(",")]
    boxes.append(coord)

distances = [[None for _ in range(len(boxes))] for _ in range(len(boxes))]
sorted_distances = []
sorted_pairs = []
for i in range(len(distances)):
    box1 = boxes[i]
    for j in range(i + 1, len(distances)):
        box2 = boxes[j]
        distance = (box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2
        if len(sorted_distances) < PAIRS or distance < sorted_distances[-1]:
            if len(sorted_distances) == PAIRS:
                sorted_distances = sorted_distances[:-1]
                sorted_pairs = sorted_pairs[:-1]
            idx = bisect.bisect_left(sorted_distances, distance)
            bisect.insort(sorted_distances, distance)
            sorted_pairs.insert(idx, [i, j])

components = []
for i in range(PAIRS):
    new_components = []
    box1, box2 = sorted_pairs[i]
    current_component = set([box1, box2])
    for component in components:
        if box1 in component or box2 in component:
            current_component = current_component.union(component)
        else:
            new_components.append(component)
    new_components.append(current_component)
    components = new_components

components.sort(key=len, reverse=True)
print(len(components[0]) * len(components[1]) * len(components[2]))
