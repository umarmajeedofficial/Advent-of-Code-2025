def max_two_digit_from_line(s: str) -> int:
    s = s.strip()
    n = len(s)
    if n < 2:
        return 0
    max_right = int(s[-1])
    best = 0
    for i in range(n - 2, -1, -1):
        max_right = max(max_right, int(s[i + 1]))
        candidate = 10 * int(s[i]) + max_right
        if candidate > best:
            best = candidate
    return best
def main():
    total = 0
    with open("input.txt", "r") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            total += max_two_digit_from_line(line)
    print(total)
if __name__ == "__main__":
    main()
