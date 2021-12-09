from math import prod
from itertools import product

from raw_input import raw_input

D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
R = [[int(c) for c in r] for r in raw_input.split("\n")]
MAX_Y, MAX_X = len(R), len(R[0])


def near(_y, _x):
    return set((y, x) for dy, dx in D if 0 <= (y := _y + dy) < MAX_Y and 0 <= (x := _x + dx) < MAX_X)


def pool(low):
    done, todo = set(), {low}

    while todo and (_next := todo.pop()):
        done.add(_next)
        todo |= set((y, x) for y, x in near(*_next) if R[y][x] != 9) - done

    return done


lows = set((y, x) for y, x in product(range(MAX_Y), range(MAX_X)) if all(R[y][x] < R[_y][_x] for _y, _x in near(y, x)))

print(f"Part 1: {sum(1 + R[y][x] for y, x in lows)}")
print(f"Part 2: {prod(sorted(map(len, [pool(l) for l in lows]))[-3:])}")
