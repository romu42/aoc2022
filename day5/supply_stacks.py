#! /usr/bin/env python3
# https://adventofcode.com/2022/day/5


def parse_input(f):
    matrix = []
    steps = []
    for line in f:
        if 'move' not in line:
            line = line.replace("[ ]", "-")
            line = line.replace("[", "")
            line = line.replace("]", "")
            matrix.append(line.rstrip())
        if 'move' in line:
            steps.append(line.rstrip().split(' '))

    steps = get_steps(steps)
    matrix = form_matrix_test(matrix)

    return steps, matrix
def get_steps(steps: list) -> list:
    movement = []
    for move in steps:
        cnt = int(move[1])
        frm = int(move[3])-1
        to = int(move[5])-1
        movement.append([cnt,frm,to])
    return movement


def form_matrix_test(matrix: list) -> list:
    stacks = []
    matrix = matrix[:-1]
    stack_count = len([x for x in matrix[-1] if x in '1234568789'])
    matrix = matrix[:-1]
    matrix = [ x.split(" ") for x in matrix]
    matrix = [[row[i] for row in matrix] for i in range(stack_count)]
    for stack in matrix:
        stack.reverse()
    for stack in matrix:
        temp_stack = stack[:]
        for crate in stack:
            if crate == '-':
                temp_stack.pop()
        stacks.append(temp_stack)
    return stacks


def reorder_crates_9000(steps, matrix: list) -> list:
    for move in steps:
        for i in range(move[0]):
            matrix[move[2]].append(matrix[move[1]].pop())
    return matrix


def reorder_crates_9001(steps, matrix: list) -> list:
    for move in steps:
        move_count = move[0]
        matrix[move[2]] = matrix[move[2]] + matrix[move[1]][-move_count:]
        del(matrix[move[1]][-move_count:])
    return matrix


def get_stack_top(matrix: list):
    answer = ""
    for stack in matrix:
        answer = answer + stack.pop()
    print(answer)


def main():
    test = True
    pt = 2
    if test:
        with open('puzzle_input_test') as f:
            steps, matrix =  parse_input(f)
    else:
        with open('puzzle_input_fixed') as f:
            steps, matrix = parse_input(f)

    if pt == 1:
        matrix = reorder_crates_9000(steps, matrix)
        get_stack_top(matrix)
    if pt == 2:
        matrix = reorder_crates_9001(steps, matrix)
        get_stack_top(matrix)


if __name__ == '__main__':
    main()