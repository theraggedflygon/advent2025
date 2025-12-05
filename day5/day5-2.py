class IDRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

with open("day5_input.txt", 'r') as file:
    range_data, _ = file.read().split("\n\n")

id_ranges = []
for row in range_data.split("\n"):
    start, end = [int(num) for num in row.split("-")]
    id_ranges.append(IDRange(start, end))

components = [None for _ in range(len(id_ranges))]
active_component = 1
for i in range(len(id_ranges)):
    if components[i] is None:
        components[i] = active_component
        active_component += 1
    for j in range(i + 1, len(id_ranges)):
        if not (id_ranges[i].start > id_ranges[j].end or id_ranges[i].end < id_ranges[j].start):
            if components[i] is not None and components[j] is None:
                components[j] = components[i]
            elif components[i] < components[j]:
                replace_component = components[j]
                for k in range(len(components)):
                    if components[k] == replace_component:
                        components[k] = components[i]
            elif components[j] < components[i]:
                replace_component = components[i]
                for k in range(len(components)):
                    if components[k] == replace_component:
                        components[k] = components[j]

component_min = [None for _ in range(active_component)]
component_max = [None for _ in range(active_component)]
for idx, id_range in enumerate(id_ranges):
    comp = components[idx]
    if component_min[comp] is None or id_range.start < component_min[comp]:
        component_min[comp] = id_range.start
    if component_max[comp] is None or id_range.end > component_max[comp]:
        component_max[comp] = id_range.end

total = 0
for i in range(active_component):
    if component_min[i] is None or component_max[i] is None:
        continue
    total += (component_max[i] - component_min[i] + 1)

print(total)
