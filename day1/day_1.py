def load_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        input = [int(x) if x != "\n" else None for x in lines]

    return input


def puzzle_1(input):
    all_elves = []
    cal_counter = 0
    for entry in input:
        if entry == None:
           all_elves.append(cal_counter)
           cal_counter = 0
        else:
            cal_counter += entry

    print("Puzzle 1: ")
    print(max(all_elves)) 
    return(all_elves)

def puzzle_2(all_elves):
    top_3 = 0
    for i in range(3):
       max_cal = max(all_elves)
       top_3 += max_cal
       all_elves.remove(max_cal) 

    print("\nPuzzle 2: ")
    print(top_3)

print("----- Day 1 -----")
input = load_input("input.txt")
all_elves = puzzle_1(input)
puzzle_2(all_elves)