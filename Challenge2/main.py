import re
import time


def get_numbers(str):
    array = re.findall(r"[0-9]+", str)
    array = [int(i) for i in array]
    return array


def part_one(lst):
    solution = 0
    for i in range(lst[0], lst[1] + 1):
        if len(str(i)) % 2 == 0:
            if str(i)[: len(str(i)) // 2] == str(i)[len(str(i)) // 2 :]:
                solution += i
    return solution


def part_two(lst):
    solution = 0
    for i in range(lst[0], lst[1] + 1):
        for j in range(1, (len(str(i)) // 2) + 1):
            if len(str(i)) % j == 0:
                if (str(i)[:j]) * (len(str(i)) // j) == str(i):
                    solution += i
                    break
    return solution


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_file = file.read().strip()
        input_lst = [get_numbers(i) for i in input_file.split(",")]

    solution = 0
    for i in input_lst:
        solution += part_one(i)
    print(f"Part 1 Solution = {solution}")

    solution = 0
    for i in input_lst:
        solution += part_two(i)
    print(f"Part 2 Solution = {solution}")
