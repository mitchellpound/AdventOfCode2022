from collections import Counter

def load_input(filename):
    with open(filename) as file:
        lines = [line.strip('\n') for line in file.readlines()]

    return lines

def make_arrays(input):
    opp_shape = [line[0] for line in input]
    mapping = {'X':'A', 'Y':'B', 'Z':'C'}
    my_shape = [mapping.get(line[-1], None) for line in input]

    return my_shape, opp_shape

def is_win(my_shape, opp_shape):
    if my_shape == 'A':
        if opp_shape == 'C':
            return True
    elif my_shape == 'B':
        if opp_shape == 'A':
            return True
    elif my_shape == 'C':
        if opp_shape == 'B':
            return True

    return False


def puzzle(input):
    my_shape, opp_shape = make_arrays(input)
    my_shape_count = Counter(my_shape)
    
    # shape score
    score = my_shape_count['A'] + my_shape_count['B'] * 2 + my_shape_count['C'] * 3

    # win score
    for i in range(len(my_shape)):
        if my_shape[i] == opp_shape[i]:
            score += 3
        if is_win(my_shape[i], opp_shape[i]):
            score += 6
        
    return score

def to_array(input):
    opp_shape = [line[0] for line in input]
    my_array = [line[-1] for line in input]

    return my_array, opp_shape

def transfor_to_shape(my_array, opp_shapes):
    # X lose
    # Y draw 
    # Z win
    mapping = {
        'A': {'X':'C', 'Y':'A', 'Z': 'B'},
        'B': {'X':'A', 'Y':'B', 'Z': 'C'},
        'C': {'X':'B', 'Y':'C', 'Z': 'A'}
    }

    shape_arr = [mapping.get(opp_shapes[i], None).get(my_array[i], 'What?') for i in range(len(my_array))]

    return shape_arr


def puzzle_2(input):
    my_array, opp_shape = to_array(input) 
    win_counter = Counter(my_array)
   
    # score from winning round
    score = win_counter['Y'] * 3 + win_counter['Z'] * 6

    # score from shape
    shape_arr = transfor_to_shape(my_array, opp_shape)
    shape_counter = Counter(shape_arr)

    score += shape_counter['A'] + shape_counter['B'] * 2 + shape_counter['C'] * 3

    return score



print("----- Day 2 -----")
input = load_input("/home/mitchlb/Coding/AdventOfCode2022/day2/input.txt")
score = puzzle(input)
print(score)
score2 = puzzle_2(input)
print(score2)