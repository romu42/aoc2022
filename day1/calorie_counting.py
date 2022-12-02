# https://adventofcode.com/2022/day/1

import re


def sum_calories(input_data: list):
    elf_by_calories = []
    calories = []

    input_data = ([x.strip() for x in input_data])
    for line in input_data:
        if re.match(r'^\s*$', line):
            total_calories = sum(calories)
            elf_by_calories.append(total_calories)
            calories = []
        else:
            calories.append(int(line))
    elf_by_calories.sort(reverse=True)
    print(sum(elf_by_calories[:1]))
    print(sum(elf_by_calories[:3]))


if __name__ == '__main__':
    with open("puzzle_input") as data:
        sum_calories(data)
