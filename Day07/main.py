import re


def find_strings(string, character):
    return [x.start() for x in re.finditer(f"\\{character}", string)]


def part_one(lst: list):
    solution = 0
    index_set = set()
    index_set.add(lst[0].index("S"))
    for line in lst[1:]:
        tmp_set = set()
        occurences = find_strings(line, "^")

        for i in occurences:
            if i in index_set:
                solution += 1
                index_set.remove(i)
                if i == 0:
                    tmp_set.add(i + 1)
                elif i == len(line) - 1:
                    tmp_set.add(i - 1)
                else:
                    tmp_set.add(i + 1)
                    tmp_set.add(i - 1)
        index_set.update(tmp_set)

    return solution


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        input = file.read().strip()

    input = input.split()
    solution = part_one(input)

    print(f"Part One Solution: {solution}")
