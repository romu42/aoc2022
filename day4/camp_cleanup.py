# https://adventofcode.com/2022/day/4

def parse_input(input_file) -> list:
    sections = []
    for line in input_file:
        line = line.strip()
        line = line.split(',')
        sections.append(line)
    return sections

def expand_sections(sections: list) -> list:
    assignments = []
    #print(sections)
    for section in sections:
        sub_list = []
        for section_part in section:
            assignment = (section_part.split('-'))
            sub_list.append([x for x in range(int(assignment[0]), int(assignment[1])+1)])
        assignments.append(sub_list)
    return assignments

def check_overlap(sections: list) -> int:
    overlap_count = 0
    total_count = 0

    for section in sections:
        flag = 0
        a_list = section[0]
        b_list = section[1]
        if (all(x in a_list for x in b_list)):
           flag = 1
        if (all(x in b_list for x in a_list)):
            flag = 1
        overlap_count = overlap_count + flag
        a_set = set(a_list)
        b_set = set(b_list)
        if (a_set & b_set):
            total_count += 1

    return overlap_count,total_count


if __name__ == "__main__":
    sections = []
    with open("puzzle_input") as file:
        sections = parse_input(file)
    sections = expand_sections(sections)
    print(check_overlap(sections))