def is_repeated_block(n: int) -> bool:
    s = str(n)
    L = len(s)
    for block_len in range(1, L // 2 + 1):
        if L % block_len != 0:
            continue
        block = s[:block_len]
        if block * (L // block_len) == s:  
            return True
    return False

def main():
    with open("Day 2\day2input.txt", "r") as f:
        line = f.read().strip()

    total_sum = 0
    ranges = line.split(",")

    for r in ranges:
        if not r:
            continue
        start, end = map(int, r.split("-"))

        for x in range(start, end + 1):
            if is_repeated_block(x):
                total_sum += x
    print(total_sum)
if __name__ == "__main__":
    main()
