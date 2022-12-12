#! /usr/bin/env python3
# https://adventofcode.com/2022/day/8
# grid[row(x)][column(y)]
# tree[x,y]


def parse_input(f):
    grid = []
    for line in f:
        line = line.rstrip()
        grid.append([int(x) for x in line])
    return grid


def set_edges(grid: list):
    north_border = 0
    east_border = len(grid[0]) - 1
    south_border = len(grid) - 1
    west_border = 0

    return north_border, east_border, south_border, west_border


def check_edge(
    north_border: int, east_border: int, south_border: int, west_border: int, tree: list
) -> bool:
    x = tree[0]
    y = tree[1]
    if x == north_border:
        return True
    elif x == east_border:
        return True
    elif x == south_border:
        return True
    elif x == west_border:
        return True
    elif y == north_border:
        return True
    elif y == east_border:
        return True
    elif y == south_border:
        return True
    elif y == west_border:
        return True
    else:
        return False


def check_north(tree, grid, border):
    # reduce x to move north
    # print(f"border {border}")
    x = tree[0]
    y = tree[1]
    scenic = 0
    for cnt in range(x - 1, border - 1, -1):
        scenic += 1
        # print(f"{cnt},{y} {grid[cnt][y]} {tree} {grid[tree[0]][tree[1]]}")
        if grid[cnt][y] >= grid[tree[0]][tree[1]]:
            # print('invisible')
            return False, scenic
    # print('visible')
    return True, scenic


def check_east(tree, grid, border):
    # increase y to move east
    #  print(f"border {border}")
    x = tree[0]
    y = tree[1]
    scenic = 0
    for cnt in range(y + 1, border + 1, +1):
        scenic += 1
        #      print(f"{x},{cnt} {grid[x][cnt]} {tree} {grid[tree[0]][tree[1]]}")
        if grid[x][cnt] >= grid[tree[0]][tree[1]]:
            #          print('invisible')
            return False, scenic
    #  print('visible')
    return True, scenic


def check_south(tree, grid, border):
    # increase x to move south
    #  print(f"border {border}")
    x = tree[0]
    y = tree[1]
    scenic = 0
    for cnt in range(x + 1, border + 1, +1):
        scenic += 1
        #      print(f"{cnt},{y} {grid[cnt][y]} {tree} {grid[tree[0]][tree[1]]}")
        if grid[cnt][y] >= grid[tree[0]][tree[1]]:
            #          print('invisible')
            return False, scenic
    #  print('visible')
    return True, scenic


def check_west(tree, grid, border):
    # decrease y to move west
    # print(f"border {border}")
    x = tree[0]
    y = tree[1]
    scenic = 0
    for cnt in range(y - 1, border - 1, -1):
        scenic += 1
        # print(f"{x},{cnt} {grid[x][cnt]} {tree} {grid[tree[0]][tree[1]]}")
        if grid[x][cnt] >= grid[tree[0]][tree[1]]:
            # print('invisible')
            return False, scenic
    # print('visible')
    return True, scenic


def check_visible(
    north_border: int, east_border: int, south_border: int, west_border: int, grid
):
    visible = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if check_north([x, y], grid, north_border):
                visible += 1
                continue
            elif check_east([x, y], grid, east_border):
                visible += 1
                continue
            elif check_south([x, y], grid, south_border):
                visible += 1
                continue
            elif check_west([x, y], grid, west_border):
                visible += 1
                continue
    print(visible)


def check_scenic(
    north_border: int, east_border: int, south_border: int, west_border: int, grid
):
    visible_cnt = 0
    scenic_best = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            scenic_values = []
            visible = False
            visible, scenic_value =  check_north([x, y], grid, north_border)
            scenic_values.append(scenic_value)
            visible, scenic_value = check_east([x, y], grid, east_border)
            scenic_values.append(scenic_value)
            visible, scenic_value = check_south([x, y], grid, south_border)
            scenic_values.append(scenic_value)
            visible, scenic_value = check_west([x, y], grid, west_border)
            scenic_values.append(scenic_value)
            if visible:
                visible_cnt += 1
            scenic_value = 1
            for value in scenic_values:
                scenic_value *= value
            if scenic_value > scenic_best:
                scenic_best = scenic_value
    print(visible_cnt, scenic_best)


def main(input_file):
    grid = parse_input(input_file)
    # print(grid)
    north_border, east_border, south_border, west_border = set_edges(grid)
    check_visible(north_border, east_border, south_border, west_border, grid)
    check_scenic(north_border, east_border, south_border, west_border, grid)


if __name__ == "__main__":
    test = False
    if test:
        with open("puzzle_input_test") as f:
            main(f)
    else:
        with open("puzzle_input") as f:
            main(f)
