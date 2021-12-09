from functools import reduce

from raw_input import raw_input

ROWS = [[int(c) for c in r] for r in raw_input.split("\n")]
MAX_Y = len(ROWS) - 1
MAX_X = len(ROWS[0]) - 1
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def neighbours(_y, _x, ignore=None, f=None):
    n = set()
    for d_y, d_x in DIRECTIONS:
        n_y, n_x = (_y + d_y, _x + d_x)

        if (not ignore or (n_y, n_x) not in ignore) \
                and 0 <= n_y <= MAX_Y \
                and 0 <= n_x <= MAX_X \
                and (not f or f(n_y, n_x)):
            n.add((n_y, n_x))

    return n


lowests = set()
for y, row in enumerate(ROWS):
    for x, col in enumerate(row):
        current = ROWS[y][x]
        lowest = True

        for d_y, d_x in neighbours(y, x):
            if ROWS[d_y][d_x] <= current:
                lowest = False

        if lowest:
            lowests.add((y, x))

pool_sizes = []
for lowest in lowests:
    explored = set()
    to_explore = {lowest}

    while to_explore:
        candidate = to_explore.pop()
        explored.add(candidate)
        to_explore = to_explore | neighbours(*candidate, ignore=explored, f=lambda _y, _x: ROWS[_y][_x] != 9)

    pool_sizes.append(len(explored))

print(f"Part 1: {sum(1 + ROWS[y][x] for y, x in lowests)}")
print(f"Part 2: {reduce((lambda _x, _y: _x * _y), sorted(pool_sizes)[-3:])}")
