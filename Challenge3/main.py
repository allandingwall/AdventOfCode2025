def part_one(line: str) -> int:
    max = int(line[0] + line[1])

    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            num = int(line[i] + line[j])
            if num > max:
                max = num
    return max


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_file = file.read().strip()
    input_lst = input_file.split("\n")

    solution = 0

    for line in input_lst:
        solution += part_one(line)

    print(f"Part One Solution: {solution}")
