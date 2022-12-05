# https://adventofcode.com/2022/day/3

def clean(file: list) -> list:
    contents = []
    for line in file:
        contents.append(line.strip())
    return contents

def fill_rucksacks(contents: list) -> list:
    #print(contents)
    for item in contents:
        split = int(len(item)/2)
        rucksacks.append([item[:split], item[split:]])
    return rucksacks

def find_common_type2(rucksacks: list) -> list:
    common_types = []
    for item in rucksacks:
    #    print(item[0])
    #    print(item[1])
        a_set = set(item[0])
        b_set = set(item[1])
        common_type = a_set & b_set
        common_types.append(common_type.pop())
    return common_types

def find_common_type3(contents: list) -> list:
    print('entering common_type3')
    common_types = []
    while len(contents) > 2:
        #print(contents[0],  contents[1], contents[2])
        a_set = set(contents[0])
        b_set = set(contents[1])
        c_set = set(contents[2])
        common_type = (a_set & b_set & c_set)
        common_types.append(common_type.pop())
        del contents[0:3]
    return common_types


def get_sum(common_types: list) -> int:
    total = 0
    priorities = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26,
    'A':27,
    'B':28,
    'C':29,
    'D':30,
    'E':31,
    'F':32,
    'G':33,
    'H':34,
    'I':35,
    'J':36,
    'K':37,
    'L':38,
    'M':39,
    'N':40,
    'O':41,
    'P':42,
    'Q':43,
    'R':44,
    'S':45,
    'T':46,
    'U':47,
    'V':48,
    'W':49,
    'X':50,
    'Y':51,
    'Z':52,
    }
    for item in common_types:
        priorities[item[0]]
        total = total + priorities[item[0]]
    return total

if __name__ == '__main__':
    rucksacks = []
    with open("puzzle_input") as file:
        contents = clean(file)
    rucksacks = fill_rucksacks(contents)
    #print(rucksacks)
    common_types = find_common_type2(rucksacks)
    #print(common_types)
    print(get_sum(common_types))
    common_types = find_common_type3(contents)
    print(get_sum(common_types))
