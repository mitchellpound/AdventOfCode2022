def get_input(filename):
    with open(filename) as file:
        lines = [line.strip('\n') for line in file.readlines()]

    return lines


def puzzle(input):
    stack = []
    dirs = {}

    for line in input:
        if line[0] == '$':
            if line[2:4] == 'ls':
                pass
            # go back a directory
            elif line[2:7] == 'cd ..':
                prev_path = tuple(stack)
                stack.pop(-1)
                after_path = tuple(stack)
                dirs[after_path] += dirs[prev_path]
            # go down a directory
            else:
                stack.append(line[5:])
                path = tuple(stack)
                dirs[path] = 0
        elif line[:3] == 'dir':
            pass
        else:
            path = tuple(stack)
            dirs[path] += int(line[:line.index(' ')])

    for _ in range(len(stack) - 1):
        prev_path = tuple(stack)
        stack.pop(-1)
        after_path = tuple(stack)
        dirs[after_path] += dirs[prev_path]
 
                    
    counter = 0
    for key, dir_size in dirs.items():
        if dir_size <= 100000:
            counter += dir_size

    return counter, dirs

def puzzle_2(dirs):
    space_needed = 30000000
    current_space = 70000000 - dirs[('/',)]

    big_enough = []
    for key, dir_space in sorted(dirs.items()):
        if dir_space >= space_needed - current_space:
            big_enough.append(dir_space)

    return min(big_enough)


print("----- Day 7 -----")
input = get_input('input.txt')

counter, dirs = puzzle(input)
print(counter)

print(puzzle_2(dirs))

