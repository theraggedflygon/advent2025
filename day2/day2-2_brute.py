with open("day2_input.txt", 'r') as file:
    ranges = file.read().split(",")

all_ranges = []
all_valid = set()
total = 0
max_val = 0
for range_data in ranges:
    start, end = [int(num) for num in range_data.split("-")]
    if end > max_val:
        max_val = end
    all_ranges.append([start, end])

max_len = len(str(max_val))

for length in range(2, max_len + 1):
    seg_num = 1
    whole_num = int(str(seg_num) * length)
    while whole_num < max_val:
        if whole_num in all_valid:
            seg_num += 1
            whole_num = int(str(seg_num) * length)
            continue
        for start, end in all_ranges:
            if start <= whole_num <= end:
                if whole_num == 666:
                    print(start, end, length)
                total += whole_num
                all_valid.add(whole_num)
                break
        seg_num += 1
        whole_num = int(str(seg_num) * length)

print(total)
