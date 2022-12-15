def load_input(filename):
    with open(filename) as file:
        data = file.read()

    return data

def puzzle(data):
    counter = 4
    while True:
        s = set(data[counter-4:counter])
        if len(s) != 4:
            counter += 1
        else:
            return counter

        if counter > len(data):
            print("oops...")
            break

def puzzle_2(data):
    counter = 14
    while True:
        s = set(data[counter-14:counter])
        if len(s) != 14:
            counter += 1
        else:
            return counter

        if counter > len(data):
            print("oops...")
            break


print("----- Day 6 -----")
data = load_input('input.txt')

print(puzzle(data))
print(puzzle_2(data))