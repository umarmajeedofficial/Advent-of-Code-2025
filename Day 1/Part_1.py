def count_zero_positions(filename: str) -> int:
    MOD = 100
    pos = 50
    zero_count = 0

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]   
            distance = int(line[1:]) 
            if direction == 'L':
                pos = (pos - distance) % MOD
            else:  
                pos = (pos + distance) % MOD

            if pos == 0:
                zero_count += 1

    return zero_count


if __name__ == "__main__":
    filename = "input.txt" 
    result = count_zero_positions(filename)
    print("Password =", result)
