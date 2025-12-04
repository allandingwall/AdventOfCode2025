def check_cell(lst: list, row: int, col: int):
    if row < 0 or row > len(lst) - 1:
        cell_value = "."
    elif col < 0 or col > len(lst[row]) - 1:
        cell_value = "."
    else:
        cell_value = lst[row][col]

    if cell_value == "@":
        return 1
    else:
        return 0


def assess_cell(lst: list, row: int, col: int):
    ctr = 0
    for row_adjust in range(-1, 2):
        for col_adjust in range(-1, 2):
            if not (row_adjust == 0 and col_adjust == 0):
                ctr += check_cell(lst, row + row_adjust, col + col_adjust)
            if ctr == 4:
                return 0
    return 1


def part_one(input_lst: list):
    solution = 0
    for row in range(len(input_lst)):
        for col in range(len(input_lst[row])):
            if input_lst[row][col] == "@":
                solution += assess_cell(input_lst, row, col)
            else:
                continue
    return solution


def part_two(input_lst: list):
    solution = 0

    while True:
        round_solution = 0
        pop_lst = []

        for row in range(len(input_lst)):
            for col in range(len(input_lst[row])):
                if input_lst[row][col] == "@":
                    if assess_cell(input_lst, row, col):
                        pop_lst.append([row, col])
                        solution += 1
                        round_solution += 1
                else:
                    continue

        if round_solution == 0:
            return solution

        else:
            for i in pop_lst:
                row = input_lst[i[0]]
                input_lst[i[0]] = row[: i[1]] + "." + row[i[1] + 1 :]


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_file = file.read().strip()
    input_lst = input_file.split("\n")

    solution = part_one(input_lst)
    print(f"Part One Solution: {solution}")

    solution = part_two(input_lst)
    print(f"Part Two Solution: {solution}")
