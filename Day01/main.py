def part_one(input_file):
    dial = 50
    ctr = 0

    for line in input_file:
        line = line.strip()
        letter = line[0]
        number = int(line[1:])

        if letter == "L":
            number *= -1

        dial = (dial + number) % 100

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

        if direction == "L":
            movement = -dist
        else:
            movement = dist

        if movement > 0:
            i = 0
            while i < movement:
                dial += 1
                i += 1

                dial = dial % 100
                if dial == 0:
                    ctr += 1

        elif movement < 0:
            i = 0
            while i > movement:
                dial -= 1
                i -= 1

                dial = dial % 100

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
