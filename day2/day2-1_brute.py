with open("day2_input.txt", 'r') as file:
    ranges = file.read().split(",")

all_ranges = []
total = 0
max_val = 0
for range_data in ranges:
    start, end = [int(num) for num in range_data.split("-")]
    if end > max_val:
        max_val = end
    all_ranges.append([start, end])

half_num = 1
whole_num = int(str(half_num) + str(half_num))
while whole_num < max_val:
    for start, end in all_ranges:
        if start <= whole_num <= end:
            total += whole_num
            break
    half_num += 1
    whole_num = int(str(half_num) + str(half_num))

print(total)
