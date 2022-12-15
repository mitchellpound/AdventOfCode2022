def load_input(filename):
    with open(filename) as file:
        lines = [line.strip('\n') for line in file.readlines()]
        
    instruct_start = lines.index("")
    instructions = lines[instruct_start + 1:]
    stack_count = int(lines[instruct_start-1].split('   ')[-1])

    stacks = [[] for i in range(1, stack_count + 1)]
    # counter for what line it is on
    for i in range(instruct_start - 2, -1, -1):
        # counter for which stack it is on 
        for j in range(stack_count):
            box = lines[i][j * 4 + 1]
            if box != ' ':
                stacks[j].append(box)

    return stacks, instructions

def puzzle(stacks, instructions):
    for line in instructions:
        movements = line.split(' ')
        for _ in range(int(movements[1])):
            stacks[int(movements[-1]) - 1].append(stacks[int(movements[3]) - 1].pop(-1))

    return stacks

def puzzle_2(stacks, instructions):
    for line in instructions:
        holder = []
        movements = line.split(' ')
        for _ in range(int(movements[1])):
            holder.append(stacks[int(movements[3]) - 1].pop(-1))

        for _ in range(int(movements[1])):
            stacks[int(movements[-1]) - 1].append(holder.pop(-1))

    return stacks


print("----- Day 5 -----")

stacks, instructions = load_input('input.txt')
stacks_2 = puzzle(stacks, instructions)

for stack in stacks_2:
    print(stack[-1])

print("--- part 2 ---")
stacks, instructions = load_input('input.txt')
stacks_3 = puzzle_2(stacks, instructions)

for stack in stacks_3:
    print(stack[-1])
