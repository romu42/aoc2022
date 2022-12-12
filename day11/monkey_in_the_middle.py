#! /usr/bin/env python3
# https://adventofcode.com/2022/day/11

def set_starting_items(line):
    line = line.strip("Starting items: ")
    line = [int(x) for x in line.split(",")]
    return line

def set_operations(line):
    _, line = line.split("=")
    old, operation, value = line.split()
    return [old, operation, value]

def set_test(line):
    line = line.strip("Test: divisible by ")
    return int(line)
def set_sant(line):
    line = line.strip("If true: throw to monkey ")
    return int(line)
def set_falsk(line):
    line = line.strip("If false: throw to monkey ")
    return int(line)
def parse_input(input_file):
    monkeys = {}
    ops = {}
    test = {}
    sant = {}
    falsk = {}
    item_count = {}
    for line in input_file:
        line = line.strip()
        if "Monkey" in line:
            monkey_number = int(line[7:8])
            monkeys[monkey_number] = []
            item_count[monkey_number] = 0
        elif "Starting items:" in line:
            monkeys[monkey_number] = set_starting_items(line)
        elif "Operation" in line:
            ops[monkey_number] = set_operations(line)
        elif "Test" in line:
            test[monkey_number] = set_test(line)
        elif "true" in line:
            sant[monkey_number] = set_sant(line)
        elif "false" in line:
            falsk[monkey_number] = set_falsk(line)

    return monkeys, ops, test, sant, falsk, item_count

def inspect_item(item, ops, test, sant, falsk):
    #print(f"inspecting item: {item}, ops: {ops}, test: {test}, sant: {sant}, falsk: {falsk}")
    if ops[2] == "old":
        if ops[1] == '*':
            item = item * item
        elif ops[1] == '+':
            item= item + item
    else:
        if ops[1] == '*':
            item = item * int(ops[2])
        elif ops[1] == '+':
            item = item + int(ops[2])

    worry_level = divmod(item, 3)
    if worry_level[0] % test == 0:
        return worry_level[0], sant
    else:
        return worry_level[0], falsk

def inspect_item2(item, ops, test, sant, falsk):
    #print(f"inspecting item: {item}, ops: {ops}, test: {test}, sant: {sant}, falsk: {falsk}")
    if ops[2] == "old":
        if ops[1] == '*':
            item = item * item
        elif ops[1] == '+':
            item= item + item
    else:
        if ops[1] == '*':
            item = item * int(ops[2])
        elif ops[1] == '+':
            item = item + int(ops[2])

    if item % test == 0:
        return item, sant
    else:
        return item, falsk

def part_1(monkeys, ops, test, sant, falsk, item_count):
    items_inspected = {}
    for count in range(20):
        for monkey in monkeys:
            #print(f"Monkey {monkey} is holding {monkeys[monkey]}")
            item_count[monkey] += len(monkeys[monkey])
            for item in monkeys[monkey]:
                worry_level, next_monkey = inspect_item(item, ops[monkey], test[monkey], sant[monkey], falsk[monkey])
                monkeys[next_monkey].append(worry_level)
            monkeys[monkey] = []
        #print(monkeys)
    monkey_counted = [x for x in item_count.values()]
    monkey_counted.sort(reverse=True)
    print(monkey_counted[0] * monkey_counted[1])

def part_2(monkeys, ops, test, sant, falsk, item_count):
    items_inspected = {}
    for count in range(10000):
        for monkey in monkeys:
            #print(f"Monkey {monkey} is holding {monkeys[monkey]}")
            item_count[monkey] += len(monkeys[monkey])
            for item in monkeys[monkey]:
                worry_level, next_monkey = inspect_item2(item, ops[monkey], test[monkey], sant[monkey], falsk[monkey])
                monkeys[next_monkey].append(worry_level)
            monkeys[monkey] = []
        #print(monkeys)
    monkey_counted = [x for x in item_count.values()]
    monkey_counted.sort(reverse=True)
    print(monkey_counted[0] * monkey_counted[1])
def main(input_file):
    monkeys, ops, test, sant, falsk, item_count = parse_input(input_file)
    #print(monkeys, "\n", ops, "\n", test, "\n", sant, "\n", falsk )
    part_1(monkeys, ops, test, sant, falsk, item_count)
    part_2(monkeys, ops, test, sant, falsk, item_count)

if __name__ == "__main__":
    test = True
    if test:
        with open("puzzle_input_test") as f:
            main(f)
    else:
        with open("puzzle_input") as f:
            main(f)