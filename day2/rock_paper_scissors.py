# https://adventofcode.com/2022/day/2

def check_score(input_data: list):
    part1_total_points = 0
    part2_total_points = 0
    for line in input_data:
        round = line.strip()

        match round:
            case "A X":
                part1_total_points += 4
                part2_total_points += 3
            case "A Y":
                part1_total_points += 8
                part2_total_points += 4
            case "A Z":
                part1_total_points += 3
                part2_total_points += 8
            case "B X":
                part1_total_points += 1
                part2_total_points += 1
            case "B Y":
                part1_total_points += 5
                part2_total_points += 5
            case "B Z":
                part1_total_points += 9
                part2_total_points += 9
            case "C X":
                part1_total_points += 7
                part2_total_points += 2
            case "C Y":
                part1_total_points += 2
                part2_total_points += 6
            case "C Z":
                part1_total_points += 6
                part2_total_points += 7
    print(f"part1 {part1_total_points}")
    print(f"part2 {part2_total_points}")


if __name__ == '__main__':
    with open("puzzle_input") as data:
        check_score(data)
