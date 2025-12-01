
pos = 50
count_zero = 0
with open("input.txt", "r") as file:
    data = file.read()
for line in data.strip().split("\n"):
    line = line.strip()
    direction = line[0]
    distance = int(line[1:])
    
    if direction == "L":
        step = -1
    else:
        step = 1

    full_cycles = distance // 100
    count_zero += full_cycles

    remaining = distance % 100

    for _ in range(remaining):
        pos = (pos + step) % 100
        if pos == 0:
            count_zero += 1

print("Password =", count_zero)
