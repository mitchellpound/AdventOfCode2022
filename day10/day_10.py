def get_input(filename):
    with open(filename) as file:
        lines = [line.strip('\n') for line in file.readlines()]

    input = [x.split(' ') if x[0] == 'a' else x for x in lines]
    return input

def puzzle(input, sig_strength_cycles):
    counter = 1
    cycle = []
    for instr in input:
        if instr == 'noop':
            # print('noop')
            cycle.append(counter)
        elif instr[0] == 'addx':
            # print('addx')
            cycle.append(counter)
            cycle.append(counter)
            counter += int(instr[1])

    sig_strength = []
    # for i in range(6):
    #     print(f"Cycle num, register ({(i * 20 + 20)} , {cycle[i * 20 + 19]})")
    #     sig_strength.append((i * 20 + 20) * cycle[i * 20 + 19])

    for signal in sig_strength_cycles:
        sig_strength.append(signal * cycle[signal - 1])

    return cycle, sum(sig_strength)

def puzzle_2(cycle):
    cpu_counter = 0
    message = []
    for i in range(6):
        crt_counter = 0
        line = []
        for j in range(40):
            if cycle[cpu_counter] <= crt_counter + 1 and cycle[cpu_counter] >= crt_counter - 1:
                line.append('#')
            else:
                line.append('.')

            crt_counter += 1
            cpu_counter += 1
        message.append(line) 

    return message

print("----- Day 10 -----")

input = get_input('input.txt')
cycle, answer_1 = puzzle(input, [20, 60, 100, 140, 180, 220])
print(answer_1)

message = puzzle_2(cycle)
with open('message.txt', 'w') as m_file:
    for row in message:
        for character in row:
            m_file.write(character)
        m_file.write('\n')

