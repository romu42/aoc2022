#! /usr/bin/env python3
# https://adventofcode.com/2022/day/5


def parse_input(f):
    datastream = []
    for line in f:
        datastream = [x for x in line]
        find_packet_marker(datastream)
        find_message_marker(datastream)


def find_packet_marker(datastream: list):
    found = False
    start = 0
    stop = 4
    while not found:
        if len(set(datastream[start:stop])) > 3:
            print(stop)
            found = True
        else:
            start += 1
            stop += 1


def find_message_marker(datastream: list):
    found = False
    start = 0
    stop = 14
    while not found:
        if len(set(datastream[start:stop])) > 13:
            print(stop)
            found = True
        else:
            start += 1
            stop += 1

def main_test():
    with open("puzzle_input_test") as f:
        parse_input(f)

def main():
    with open("puzzle_input") as f:
        parse_input(f)

if __name__ == '__main__':
    test = False
    if test:
        main_test()
    else:
        main()