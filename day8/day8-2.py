import bisect

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
        idx = bisect.bisect_left(sorted_distances, distance)
        bisect.insort(sorted_distances, distance)
        sorted_pairs.insert(idx, [i, j])

components = []
i = 0
while True:
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
    if len(components[0]) == len(boxes):
        print(boxes[box1][0] * boxes[box2][0])
        break
    i += 1
