def load_input(filename):
    with open(filename) as file:
        lines = [line.strip('\n') for line in file.readlines()]
        lines = [line.split(',') for line in lines]
        data = [[pair[0].split('-'), pair[1].split('-')] for pair in lines]

    return data


def puzzle(data):
    counter = 0
    for pair in data:
        p1start, p1end = pair[0]
        p2start, p2end = pair[1]

        a = set(range(int(p1start),int(p1end)+1))
        b = set(range(int(p2start),int(p2end)+1))

        c = a.intersection(b)
        if c == a or c == b:
            counter += 1
        
    return counter

def puzzle_2(data):
    counter = 0
    for pair in data:
        p1start, p1end = pair[0]
        p2start, p2end = pair[1]

        a = set(range(int(p1start),int(p1end)+1))
        b = set(range(int(p2start),int(p2end)+1))

        c = a.intersection(b)
        if c != set():
            counter += 1
        
    return counter



print("----- Day 4 -----")

data = load_input('input.txt')
print(puzzle(data))
print(puzzle_2(data))