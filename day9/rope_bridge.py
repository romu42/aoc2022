#! /usr/bin/env python3
# https://adventofcode.com/2022/day/9
# U : x + 1 # D : x - 1 # R : y + 1 # L : y - 1

def move_head(head: list, move_dir: str) -> list:
    #print("##################")
    #print(f"start move {head}")
    #print(move_dir)
    match move_dir:
        case "U":
            head[0] = head[0] + 1
        case "D":
            head[0] = head[0] - 1
        case "R":
            head[1] = head[1] + 1
        case "L":
            head[1] = head[1] - 1
    #print(f"end move with {head}")
    return head


def move_tail(head: list, tail: list) -> list:
    # [2,-1][2,0][2,1]
    # [0,-2][0,0][0,2]
    # [-2,-1][-2,0][-1,2]
    delta_x = head[0] - tail[0]
    delta_y = head[1] - tail[1]
    #print(f"head at {head} tail at {tail}")
    #print(f"case: {[delta_x, delta_y]}")
    match [delta_x, delta_y]:
        # top-left
        case [2,-1]:
            tail = [tail[0]+1,tail[1]-1]
        case [1,-2]:
            tail = [tail[0]+1,tail[1]-1]
        # top
        case [2,0]:
            tail = [tail[0]+1,tail[1]]
        # top-right
        case [2,1]:
            tail = [tail[0]+1,tail[1]+1]
        case [1,2]:
            tail = [tail[0]+1,tail[1]+1]
        # right
        case [0,2]:
            tail = [tail[0],tail[1]+1]
        # bottom-right
        case [-2,1]:
            tail = [tail[0]-1,tail[1]+1]
        case [-1, 2]:
            tail = [tail[0]-1,tail[1]+1]
        # bottom
        case [-2,0]:
            tail = [tail[0]-1,tail[1]]
        # bottom-left
        case [-2,-1]:
            tail = [tail[0]-1,tail[1]-1]
        case [-1,-2]:
            tail = [tail[0]-1,tail[1]-1]
        # left
        case [0,-2]:
            tail = [tail[0],tail[1]-1]
    #print(f" after move: head at {head} tail at {tail}")
    return tail

def add_tail_pos(tail_history: list, tail:list) -> list:
    if tail not in tail_history:
        tail_history.append(tail)
    return tail_history

def part1(input_file):
    head = [0,0]
    tail = [0,0]
    tail_history = [[0,0]]
    head_path = [[0,0]]
    tail_path = [[0,0]]
    for line in input_file:
        move_dir, move_count = (line.rstrip().split())
        move_count = int(move_count)
        for _ in range(move_count):
            head = move_head(head, move_dir)
            tail = move_tail(head, tail)
#            head_path.append(head)
#            tail_path.append(tail)
            tail_history = add_tail_pos(tail_history, tail)
    print(len(tail_history))
def part2(input_file):
    rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    tail_history = []
    for line in input_file:
        move_dir, move_count = (line.rstrip().split())
        move_count = int(move_count)
        for _ in range(move_count):
            head = 0
            rope[head] = move_head(rope[head], move_dir)
            for x in range(1,len(rope)):
                tail = x
                #print(f"head is {head}")
                #print(f"tail is {tail}")
                #print(f"pre-move: head {rope[head]} , tail {rope[tail]}")
                rope[tail] = move_tail(rope[head], rope[tail])
                #print(f"post-move: head {rope[head]} , tail {rope[tail]}")
                head = tail
            tail_history = add_tail_pos(tail_history, rope[tail])
    print(len(tail_history))
def main(input_file):
    #part1(input_file)
    part2(input_file)


if __name__ == "__main__":
    test = True
    if test:
        with open("puzzle_input_test") as f:
            main(f)
    else:
        with open("puzzle_input") as f:
            main(f)
