import math


def part_one(lst: list) -> int:
    if lst[-1] == "+":
        solution = sum(lst[:-1])
    else:
        solution = math.prod(lst[:-1])
    return solution


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input = file.read().strip()

    input = input.split("\n")
    split_input = []

    for row in range(len(input)):
        if row != len(input) - 1:
            lst = [int(i) for i in input[row].split()]
        else:
            lst = input[row].split()
        split_input.append(lst)

    split_input_2 = []
    [split_input_2.append([]) for i in range(len(split_input[0]))]

    for row in range(len(split_input)):
        for col in range(len(split_input[row])):
            split_input_2[col].append(split_input[row][col])

    solution = 0
    for col in split_input_2:
        solution += part_one(col)

    print(f"Part One Solution: {solution}")
