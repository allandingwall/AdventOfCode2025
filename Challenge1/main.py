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

        start = dial
        end = (dial + movement) % 100

        # Count zero hits during the rotation (excluding final landing)
        # For right turns: positions are start+1, start+2, ..., start+movement
        # For left turns: positions are start-1, start-2, ..., start-dist
        if movement > 0:
            # R rotation: hits when (start + k) % 100 == 0
            # Solve k ≡ -start mod 100 => k = (100 - start)
            first_k = (100 - start) % 100
            if first_k == 0:
                first_k = 100  # implies exactly at 100th click

            if first_k <= movement:
                # Number of occurrences: one every 100 clicks
                ctr += 1 + (movement - first_k) // 100

        elif movement < 0:
            # L rotation: movement negative
            # hits when (start - k) % 100 == 0
            # Solve k ≡ start mod 100 => k = start
            first_k = start % 100

            if first_k == 0:
                first_k = 100  # exactly at 100th click

            kmax = -movement  # total number of clicks

            if first_k <= kmax:
                ctr += 1 + (kmax - first_k) // 100

        # Count the final landing click if it is zero
        if end == 0:
            ctr += 1

        dial = end

    return ctr


if __name__ == "__main__":
    file = open("input.txt", "r")
    part_one_result = part_one(file)
    print(part_one_result)

    file.seek(0)
    part_two_result = part_two(file)
    print(part_two_result)
