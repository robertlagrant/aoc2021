import re
from collections import defaultdict
from itertools import repeat

from raw_input import raw_input


def count_points(raw_in, include_diagonals=True):
    points = defaultdict(int)

    for raw_line in raw_in.split("\n"):
        p1x, p1y, p2x, p2y = map(int, re.match(r"(\d+),(\d+) -> (\d+),(\d+)", raw_line).groups())

        if p1x != p2x and p1y != p2y and not include_diagonals:
            continue

        for (x, y) in zip(
                repeat(p1x) if p1x == p2x else range(p1x, (p2x + (direction := 1 if p1x < p2x else -1)), direction),
                repeat(p1y) if p1y == p2y else range(p1y, (p2y + (direction := 1 if p1y < p2y else -1)), direction)):
            points[(x, y)] += 1

    return points


print(f"Part 1: {sum(1 for num in count_points(raw_input, include_diagonals=False).values() if num >= 2)}")
print(f"Part 2: {sum(1 for num in count_points(raw_input).values() if num >= 2)}")
