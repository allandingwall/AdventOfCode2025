def part_one(input_file):
    dial = 50
    ctr = 0

    for line in input_file:
        line = line.strip()
        direction = line[0]
        dist = int(line[1:])

        if direction == "L":
            dist *= -1

        dial = (dial + dist) % 100

        if dial == 0:
            ctr += 1

    return ctr


def part_two(input_file):
    dial = 50
    ctr = 0

    for line in input_file:
        line = line.strip()
        direction = line[0]
        dist = int(line[1:])

        step = 1 if direction == "R" else -1

        for _ in range(dist):
            dial += step
            dial %= 100

            if dial == 0:
                ctr += 1

    return ctr


if __name__ == "__main__":
    file = open("input.txt", "r")
    part_one_result = part_one(file)
    print(f"Part One Solution: {part_one_result}")

    file.seek(0)
    part_two_result = part_two(file)
    print(f"Part Two Solution: {part_two_result}")
