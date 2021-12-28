from enum import Enum

DEPTH = 0
POS_X = 0
AIM = 0


class Direction(Enum):
    forward = "forward"
    down = "down"
    up = "up"


def update1(current_direction, x):
    global DEPTH
    global POS_X

    if Direction.forward == current_direction:
        POS_X += x
    elif Direction.up == current_direction:
        DEPTH -= x
    else:
        DEPTH += x


def update2(current_direction, x):
    global DEPTH
    global POS_X
    global AIM

    if Direction.down == current_direction:
        AIM += x
    elif Direction.up == current_direction:
        AIM -= x
    else:
        POS_X += x
        DEPTH += AIM * x


def get_input(path):
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            direction, num = line.rstrip().split()
            num = int(num)
            yield Direction(direction), int(num)


f = get_input("input_demo.txt")
[update1(*i) for i in f]
print(POS_X, DEPTH)
print(POS_X*DEPTH)

POS_X = 0
DEPTH = 0
f = get_input("input_demo.txt")
[update2(*i) for i in f]
print(POS_X, DEPTH)
print(POS_X*DEPTH)


