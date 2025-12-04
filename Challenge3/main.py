import numpy as np


# Solves both part 1 and 2
def list_to_number(lst: list) -> int:
    num = 0
    for i in range(len(lst)):
        num += lst[i]
        if i != len(lst) - 1:
            num *= 10
    return num


def get_max_number(line: str, length: int, answer_lst=[]) -> int:
    line_list = [int(i) for i in list(line)]

    if len(line_list) == length:
        answer_lst += line_list
        return list_to_number(answer_lst)

    if length != 1:
        sub_list = line_list[: -(length - 1)]
    else:
        sub_list = line_list

    index_max = int(np.argmax(sub_list))
    answer_lst.append(sub_list[index_max])
    line = line[index_max + 1 :]
    length -= 1

    if length == 0:
        return list_to_number(answer_lst)
    else:
        return get_max_number(line, length, answer_lst)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input_file = file.read().strip()
    input_lst = input_file.split("\n")

    solution = 0
    for line in input_lst:
        solution += get_max_number(line, length=2, answer_lst=[])
    print(f"Part One Solution: {solution}")

    solution = 0
    for line in input_lst:
        solution += get_max_number(line, length=12, answer_lst=[])

    print(f"Part Two Solution: {solution}")
