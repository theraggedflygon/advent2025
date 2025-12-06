with open("day2_input.txt", 'r') as file:
    ranges = file.read().split(",")


total = 0
all_valid = set()

global_max_len = 0
all_ranges = []
for range_data in ranges:
    start, end = [int(num) for num in range_data.split("-")]

    min_len = len(str(start))
    max_len = len(str(end))
    if max_len > global_max_len:
        global_max_len = max_len
    all_ranges.append([start, end, min_len, max_len])

for REPEAT_COUNT in range(2, global_max_len + 1):
    for start, end, min_len, max_len in all_ranges:
        target_length = min_len
        if target_length % REPEAT_COUNT != 0:
            target_length += REPEAT_COUNT - (target_length % REPEAT_COUNT)
        while target_length <= max_len:
            start_array = [int(num) for num in str(start)]
            repeat_len = target_length // REPEAT_COUNT
            test_segment = [0 for _ in range(repeat_len)]
            if target_length > min_len:
                test_segment[0] = 1
                test_segment = int("".join([str(num) for num in test_segment]))
            else:
                for i in range(repeat_len):
                    test_segment[i] = start_array[i]
                test_segment = int("".join([str(num) for num in test_segment]))

            if max_len == target_length:
                end_num = end
            else:
                end_num = int("".join(["9" for _ in range(target_length)]))
            
            test_num = int(str(test_segment) * REPEAT_COUNT)
            if test_num < start:
                test_segment += 1
                test_num = int(str(test_segment) * REPEAT_COUNT)

            while test_num <= end_num:
                if test_num not in all_valid:
                    total += test_num
                    all_valid.add(test_num)
                test_segment += 1
                test_num = int(str(test_segment) * REPEAT_COUNT)

            target_length += REPEAT_COUNT

print(total)

al_list = list(all_valid)
al_list.sort()
with open("test.txt", 'a') as file:
    file.write("\n")
    file.write(str(al_list))