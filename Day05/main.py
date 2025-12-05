def part_one(id: int, fresh_id_ranges: list) -> int:
    for ranges in fresh_id_ranges:
        # ID smaller than range
        if id < ranges[0]:
            return 0
        elif ranges[0] <= id <= ranges[1]:
            return 1
        # ID larger than range
        elif ranges[1] < id:
            continue
    return 0


def part_two(fresh_id_ranges: list) -> int:
    solution = 0
    curr_start, curr_end = fresh_id_ranges[0]

    for start, end in fresh_id_ranges[1:]:
        if start <= curr_end:
            curr_end = max(curr_end, end)
        else:
            solution += curr_end - curr_start + 1
            curr_start, curr_end = start, end

    solution += curr_end - curr_start + 1
    return solution


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input = file.read().strip()

    a, b = input.split("\n\n")
    fresh_id_ranges = sorted([list(map(int, r.split("-"))) for r in a.splitlines()])
    available_ids = list(map(int, b.splitlines()))

    solution = 0
    for id in available_ids:
        solution += part_one(id, fresh_id_ranges)
    print(f"Part One Solution: {solution}")

    solution = part_two(fresh_id_ranges)
    print(f"Part Two Solution: {solution}")
