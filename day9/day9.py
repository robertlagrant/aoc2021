from math import prod
from itertools import product

from raw_input import raw_input

R = [[int(c) for c in r] for r in raw_input.split("\n")]
MAX_Y, MAX_X = len(R), len(R[0])


def near(_y, _x, ignore=None, _filter=None):
    return set(
        (_y + d_y, _x + d_x)
        for d_y, d_x in [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if (not ignore or (_y + d_y, _x + d_x) not in ignore)
        and 0 <= _y + d_y < MAX_Y
        and 0 <= _x + d_x < MAX_X
        and (not _filter or _filter(_y + d_y, _x + d_x))
    )


def pool(low):
    done, todo = set(), {low}

    while todo and (_next := todo.pop()):
        done.add(_next)
        todo = todo | near(*_next, ignore=done, _filter=lambda _y, _x: R[_y][_x] != 9)

    return done


lows = set((y, x) for y, x in product(range(MAX_Y), range(MAX_X)) if all(R[y][x] < R[_y][_x] for _y, _x in near(y, x)))

print(f"Part 1: {sum(1 + R[y][x] for y, x in lows)}")
print(f"Part 2: {prod(sorted(map(len, [pool(l) for l in lows]))[-3:])}")
