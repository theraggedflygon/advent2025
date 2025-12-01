import os

DAY = 1

if not os.path.exists(f"day{DAY}"):
    os.mkdir(f"day{DAY}")

for file_end in ["-1.py", "-2.py", "_input.txt"]:
    file = open(f"day{DAY}/day{DAY}{file_end}", 'w')
    file.close()
