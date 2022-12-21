# I'm going to do this one object oriented since it sounds kind of fun :)
def get_input(filename):
    with open(filename) as file:
        lines = [line.strip('\n').split(' ') for line in file.readlines()]

    return lines

class Head:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_head(self, dir):
        if dir == 'L':
            self.x -= 1
        elif dir == 'R':
            self.x += 1
        elif dir == 'U':
            self.y += 1
        elif dir == 'D':
            self.y -= 1
        else:
            print("Something went wrong...")

class Tail:
    def __init__(self) -> None:
        # define 'absolute' reference for position
        self.abs_x = 0
        self.abs_y = 0
        self.head = Head()
        self.visited = {(0,0)}
        
        # define 'relative' position to head
        self.relative_x = 0
        self.relative_y = 0
    
    def move_tail(self):
        # update relative position
        self.relative_x = self.abs_x - self.head.x
        self.relative_y = self.abs_y - self.head.y

        # move tail to be adjacent to head
        # directly up/ down/ right/ left
        if self.relative_x == 0:
            if self.relative_y in [0, 1, -1]:
                pass
            elif self.relative_y == -2:
                self.abs_y += 1
            elif self.relative_y == 2:
                self.abs_y -= 1
        elif self.relative_y == 0:
            if self.relative_x in [1, -1]:
                pass
            elif self.relative_x == -2:
                self.abs_x += 1
            elif self.relative_x == 2:
                self.abs_x -= 1

        # diagonal movements
        elif self.relative_x > 0:
            if self.relative_x == 1 and self.relative_y == 1:
                pass
            elif self.relative_x == 1 and self.relative_y == -1:
                pass
            elif self.relative_y > 0:
                self.abs_x -= 1
                self.abs_y -= 1
            elif self.relative_y < 0:
                self.abs_x -= 1
                self.abs_y += 1
            else:
                print("Something went wrong in the +x diagonal")
        elif self.relative_x < 0:
            if self.relative_x == -1 and self.relative_y == 1:
                pass
            elif self.relative_x == -1 and self.relative_y == -1:
                pass
            elif self.relative_y > 0:
                self.abs_x += 1
                self.abs_y -= 1
            elif self.relative_y < 0:
                self.abs_x += 1
                self.abs_y += 1
            else:
                print("Someting went wrong in the -x diagonal")
        else:
            print("Something went wrong in the whole thing")

    def do_direction(self, dir, movement):
        for i in range(movement):
            self.head.move_head(dir)
            self.move_tail()
            self.visited.add((self.abs_x, self.abs_y))

class Knot:
    def __init__(self, head) -> None:
        self.x = 0 # absolute positioning
        self.y = 0 
        self.relative_x = 0 # relative positioning
        self.relative_y = 0
        self.head = head

    def move_knot(self):
        # update relative position
        self.relative_x = self.x - self.head.x
        self.relative_y = self.y - self.head.y

        # move tail to be adjacent to head
        # directly up/ down/ right/ left
        if self.relative_x == 0:
            if self.relative_y in [0, 1, -1]:
                pass
            elif self.relative_y == -2:
                self.y += 1
            elif self.relative_y == 2:
                self.y -= 1
        elif self.relative_y == 0:
            if self.relative_x in [1, -1]:
                pass
            elif self.relative_x == -2:
                self.x += 1
            elif self.relative_x == 2:
                self.x -= 1

        # diagonal movements
        elif self.relative_x > 0:
            if self.relative_x == 1 and self.relative_y == 1:
                pass
            elif self.relative_x == 1 and self.relative_y == -1:
                pass
            elif self.relative_y > 0:
                self.x -= 1
                self.y -= 1
            elif self.relative_y < 0:
                self.x -= 1
                self.y += 1
            else:
                print("Something went wrong in the +x diagonal")
        elif self.relative_x < 0:
            if self.relative_x == -1 and self.relative_y == 1:
                pass
            elif self.relative_x == -1 and self.relative_y == -1:
                pass
            elif self.relative_y > 0:
                self.x += 1
                self.y -= 1
            elif self.relative_y < 0:
                self.x += 1
                self.y += 1
            else:
                print("Someting went wrong in the -x diagonal")
        else:
            print("Something went wrong in the whole thing")

   
class Rope:
    def __init__(self, num_knots) -> None:
        self.knots = []
        self.head = Head()
        self.knots.append(Knot(self.head))
        self.end_visited = set()
        for i in range(num_knots - 1):
            self.knots.append(Knot(self.knots[-1]))

    def do_direction(self, dir, movement):
        for i in range(movement):
            self.head.move_head(dir)
            for knot in self.knots:
                knot.move_knot()            

            # print(f"Head: ({self.head.x}, {self.head.y})")
            # for i in range(len(self.knots)):
            #     print(f"Knot {i}: ({self.knots[i].x}, {self.knots[i].y})")
            
            # print("----")
            self.end_visited.add((self.knots[-1].x, self.knots[-1].y))



def puzzle(input):
    rope = Tail()
    for line in input:
        rope.do_direction(line[0], int(line[1]))

    return len(rope.visited)

def puzzle_2(input):
    rope = Rope(9)
    for line in input:
        rope.do_direction(line[0], int(line[1]))

    return len(rope.end_visited)


print("----- Day 9 -----")
input = get_input('input.txt')
print(puzzle(input))

print(puzzle_2(input))