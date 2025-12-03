with open("day3_input.txt", 'r') as file:
    banks = file.read().split("\n")

total_volts = 0
for bank in banks:
    nums = [int(c) for c in bank]
    max_num = 0
    early_idx = 0
    for idx, num in enumerate(nums[:-1]):
        if num > max_num:
            max_num = num
            early_idx = idx
    
    second_max_num = 0
    for num in nums[early_idx + 1:]:
        if num > second_max_num:
            second_max_num = num
    
    voltage = int(str(max_num) + str(second_max_num))
    total_volts += voltage

print(total_volts)
