with open("day5_input.txt", 'r') as file:
    range_data, id_data = file.read().split("\n\n")

ranges = []
for row in range_data.split("\n"):
    start, end = [int(num) for num in row.split("-")]
    added = False
    for i in range(len(ranges)):
        if ranges[i][0] < start < ranges[i][1] and end > ranges[i][1]:
            ranges[i][1] = end
            added = True
            break
        elif ranges[i][0] < end < ranges[i][1] and start < ranges[i][0]:
            ranges[i][0] = start
            added = True
            break
    if not added:
        ranges.append([start, end])

id_list = [int(row) for row in id_data.split("\n")]

count = 0
for num in id_list:
    for start, end in ranges:
        if start <= num <= end:
            count += 1
            break

print(count)
    