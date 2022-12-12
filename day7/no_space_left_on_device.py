#! /usr/bin/env python3
# https://adventofcode.com/2022/day/7

from collections import defaultdict
class Directory:
    parent = None

    def __init__(self, name: str):
        self.name = name
        self.dirs = []
        self.files = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def hello(self):
        print(f"hey i am {self.name} and my parent is {self.parent}")

class File:
    def __init__(self, name: str, size:str):
        self.name = name
        self.size = int(size)

    def hello(self):
        print(f"hey i am {self.name} and my size is {self.size}")
def create_dir(directories: defaultdict, dir_name: str, wd: str):
    d = Directory(dir_name)
    d.parent = wd
    directories[wd].dirs.append(d)
    directories[dir_name] = d
    return directories

def initiate(directories: defaultdict, dir_name: str, wd: str):
    print('initiating parent node')
    d = Directory(dir_name)
    directories[dir_name] = d
    return directories

def ls():
    """ $ ls can be ignored I think
    """
    #print("ls: add dirs and files to wd if they do not all ready exist')
    print("ls: ignoring ls for now")

def create_files(directories, wd, file_name, size):
    file = File(file_name, size)
    directories[wd].files.append(file)
    return directories

def cd():
    print("cd: changes WD")
def parse_input(f, directories, wd):
    for line in f:
        line = line.rstrip()
        if '$ ls' == line: #done
            print(f" ls found: -> {line}")
            continue
        if 'dir ' in line: # done
            _, dir_name = line.split()
            print(f" dir found: -> {dir_name}")
            if dir_name in directories.keys():
                continue
            else:
                directories = create_dir(directories,dir_name, wd)
            directories[dir_name].hello()
            continue
        if line[0].isalnum(): #done
            size, file_name = line.split()
            size = int(size)
            print(f" file found: -> {file_name} {size}")
            if file_name in directories[wd].files:
                continue
            else:
                directories = create_files(directories,wd, file_name, size)
                continue
        if '$ cd /' == line: #done
            directories = initiate(directories, '/', wd)
            directories['/'].hello()
            wd = '/'
            continue
        if '$ cd ..' == line: # done
            print(f" cd ..  found: -> {line}")
            print(directories[wd].parent)
            continue
        if 'cd' in line: # done
            _, _, dir_name = line.split()
            print(f" cd dir  found: -> {dir_name}")
            wd = dir_name
    return directories
def main_test():
    wd = ''
    directories = defaultdict(list)
    with open("puzzle_input_test") as f:
        directories = parse_input(f, directories, wd)
    print(directories)


def main():
    with open("puzzle_input") as f:
        parse_input(f)

if __name__ == '__main__':
    test = True
    if test:
        main_test()
    else:
        main()