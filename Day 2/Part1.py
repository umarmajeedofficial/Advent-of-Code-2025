def is_repeated_pattern(n: int) -> bool:

    s = str(n)
    length = len(s)
    if length % 2 != 0:  
        return False
    mid = length // 2
    return s[:mid] == s[mid:]
def main():
    with open("input.txt", "r") as f:
        line = f.read().strip()

    total_sum = 0
    ranges = line.split(",")
    for r in ranges:
        if not r:
            continue
        start, end = map(int, r.split("-"))
        for x in range(start, end + 1):
            if is_repeated_pattern(x):
                total_sum += x
    print(total_sum)
if __name__ == "__main__":
    main()
