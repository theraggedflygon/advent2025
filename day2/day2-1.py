with open("day2_input.txt", 'r') as file:
    ranges = file.read().split(",")


total = 0
for range_data in ranges:
    start, end = [int(num) for num in range_data.split("-")]

    min_len = len(str(start))
    max_len = len(str(end))

    target_length = min_len
    if min_len % 2 == 1:
        target_length += 1
    

    while target_length <= max_len:
        start_array = [int(num) for num in str(start)]
        half_target = target_length // 2
        test_half = [0 for _ in range(half_target)]
        if target_length > min_len:
            test_half[0] = 1
            test_half = int("".join([str(num) for num in test_half]))
        else:
            for i in range(half_target):
                test_half[i] = start_array[i]
            test_half = int("".join([str(num) for num in test_half]))
            if min_len % 2 == 0:
                if test_half < int("".join([str(num) for num in start_array[half_target:]])):
                    test_half += 1

        if max_len == target_length:
            end_num = end
        else:
            end_num = int("".join(["9" for _ in range(target_length)]))
        
        test_num = int(str(test_half) + str(test_half))
        while test_num <= end_num:
            total += test_num
            test_half += 1
            test_num = int(str(test_half) + str(test_half))

        target_length += 2

print(total)
