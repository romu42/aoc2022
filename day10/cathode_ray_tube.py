#! /usr/bin/env python3
# https://adventofcode.com/2022/day/10

def add_instruction(line: str, cycle: int, x: int, signal_strength: int):
    #print(line, cycle)
    if "noop" in line:
        cycle += 1
        signal_strength = calculate_signal(cycle, x, signal_strength)
        return cycle, x, signal_strength
    else:
        instruction, value = line.split()
        value = int(value)
        cycle += 1
        signal_strength = calculate_signal(cycle, x, signal_strength)
        cycle += 1
        signal_strength = calculate_signal(cycle, x, signal_strength)
        x = x + value
        return cycle, x, signal_strength


def calculate_signal(cycle: int, x: int, signal_strength: int):
    match cycle:
        case 20:
            print(f"20 cycle:{cycle}, value:{x}, signal strength:{cycle * x}")
            return signal_strength + cycle * x
        case 60:
            print(f"60 cycle:{cycle}, value:{x}, signal strength:{cycle * x}")
            return signal_strength + cycle * x
        case 100:
            print(f"100 cycle:{cycle}, value:{x}, signal strength:{cycle * x}")
            return signal_strength + cycle * x
        case 140:
            print(f"140 cycle:{cycle}, value:{x}, signal strength:{cycle * x}")
            return signal_strength + cycle * x
        case 180:
            print(f"180 cycle:{cycle}, value:{x}, signal strength:{cycle * x}")
            return signal_strength + cycle * x
        case 220:
            print(f"220 cycle:{cycle}, value:{x}, signal strength:{cycle * x}")
            return signal_strength + cycle * x
    return signal_strength



def parse_input(input_file):
    cycle = 0
    x = 1
    signal_strength = 0
    for line in input_file:
        line = line.rstrip()
        cycle, x, signal_strength = add_instruction(line, cycle, x, signal_strength)
#        print(f"cycle:{cycle}, value:{x}, signal strength:{signal_strength}")
        print(f"signal strength: {signal_strength}")


def main(input_file):
    parse_input(input_file)


if __name__ == "__main__":
    test = False
    if test:
        with open("puzzle_input_test") as f:
            main(f)
    else:
        with open("puzzle_input") as f:
            main(f)
