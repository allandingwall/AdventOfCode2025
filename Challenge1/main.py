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
        letter = line[0]
        number = int(line[1:])

        if letter == "L":
            number *= -1

        dial += number

        if dial == 0:
            ctr += 1

        while dial < 0 or dial > 99:
            if dial < 0:
                dial += 100
                ctr += 1
            elif dial > 99:
                dial -= 100
                ctr += 1

    return ctr


if __name__ == "__main__":
    file = open("input.txt", "r")
    part_one_result = part_one(file)
    print(part_one_result)

    file.seek(0)
    part_two_result = part_two(file)
    print(part_two_result)
