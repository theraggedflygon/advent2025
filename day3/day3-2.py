VOLTAGE_LEN = 12

with open("day3_input.txt", 'r') as file:
    banks = file.read().split("\n")

total_volts = 0
for bank in banks:
    nums = [int(c) for c in bank]
    voltages = [0 for _ in range(VOLTAGE_LEN)]
    start_idx = 0
    for i in range(VOLTAGE_LEN):
        max_num = 0
        early_idx = 0
        for j in range(start_idx, len(bank) + 1 -  (VOLTAGE_LEN - i)):
            if nums[j] > max_num:
                max_num = nums[j]
                early_idx = j
        voltages[i] = max_num
        start_idx = early_idx + 1

    voltage = int("".join([str(num) for num in voltages]))
    total_volts += voltage

print(total_volts)
