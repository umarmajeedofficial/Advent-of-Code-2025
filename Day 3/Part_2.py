def max_number_12_digits(s: str) -> int:
    k = 12
    n = len(s)
    to_remove = n - k
    stack = []
    for ch in s:
        while to_remove and stack and stack[-1] < ch:
            stack.pop()
            to_remove -= 1
        stack.append(ch)
    result = ''.join(stack[:k])
    return int(result)
def main():
    total = 0
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += max_number_12_digits(line)
    print(total)
if __name__ == "__main__":
    main()
