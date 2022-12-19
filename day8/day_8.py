import numpy as np

def get_input(filename):
    with open(filename) as file:
        lines = [x.strip('\n') for x in file.readlines()]
        data = []
        for line in lines:
            data.append([int(x) for x in line])

    return np.array(data) 

def puzzle(input):
    counter = 0
    # iterate across rows
    for i in range(1, input.shape[0] - 1):
        # iterate across cols 
        for j in range(1, input.shape[1] - 1):
            left = input[i,:j].max()
            right = input[i,j+1:].max()
            top = input[:i, j].max()
            bottom = input[i+1:, j].max()

            if input[i, j] > min([left, right, top, bottom]):
                counter += 1

    counter += 2 * input.shape[0] + 2 * input.shape[1] - 4
    return counter

def puzzle_2(input):
    # iterate across rows
    optimal_scenery = 0
    for i in range(1, input.shape[0] - 1):
        # iterate across cols 
        for j in range(1, input.shape[1] - 1):
            left = np.flip(input[i,:j], 0)
            right = input[i,j+1:]
            top = np.flip(input[:i, j], 0)
            bottom = input[i+1:, j]

            tree_dist = []
            for direction in [left, right, top, bottom]:
                counter = 0
                for tree in direction:
                    if tree >= input[i,j]:
                        counter += 1
                        break

                    counter += 1

                tree_dist.append(counter)

            if np.prod(tree_dist) > optimal_scenery:
                optimal_scenery = np.prod(tree_dist)

    return optimal_scenery
                    





print("----- Day 8 -----")

input = get_input("input.txt")
print(puzzle(input))

print(puzzle_2(input))
