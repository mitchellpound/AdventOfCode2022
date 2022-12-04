from collections import Counter

def load_input(filename):
    with open(filename) as file:
        lines = [line.strip('\n') for line in file.readlines()]

    return lines

def split_sacks(lines):
    sacks = []
    for line in lines:
        compartment_1 = set(line[:(int(len(line) / 2))])
        compartment_2 = set(line[int(-len(lines) / 2):])

        if len(compartment_1) != len(compartment_2):
            print("Something went wrong with compartment indexing")
            print(len(line))
            print(len(compartment_1), len(compartment_2))
        
        sacks.append([compartment_1, compartment_2])

    return sacks

def puzzle(lines):
    total = []
    for line in lines:
        comp_1 = set(line[:int(len(line) / 2)])
        common = [x for x in comp_1.intersection(set(line[-int(len(line) / 2):]))]
        if common[0] == "":
            print("Something went wrong with the set...")
        
        total.append(common[0])

    lower = [ord(x) - 96 for x in total if x.islower()]
    upper = [ord(x) - 38 for x in total if x.isupper()]

    return sum(lower) + sum(upper)

def puzzle_2(lines):
    total = []
    for i in range(int(len(lines) / 3)):
        elf_1 = set(lines[3 * i])
        elf_2 = set(lines[3 * i + 1])
        elf_3 = set(lines[3 * i + 2])

        total.append([x for x in elf_1.intersection(elf_2, elf_3)][0])

    lower = [ord(x) - 96 for x in total if x.islower()]
    upper = [ord(x) - 38 for x in total if x.isupper()]

    return sum(lower) + sum(upper)


print("----- Day 3 -----")

lines = load_input("input.txt")
print(puzzle(lines))
print(puzzle_2(lines))