import re

from raw_input import raw

RAW_REGEX = r"target area: x=(?P<x1>-?\d+)\.\.(?P<x2>-?\d+), y=(?P<y1>-?\d+)..(?P<y2>\-?\d+)"
x1, x2, y1, y2 = map(int, re.match(RAW_REGEX, raw).groups())


def step(pos, vel):
    (x_pos, y_pos), (x_vel, y_vel) = pos, vel

    x_pos += x_vel
    y_pos += y_vel

    x_vel = x_vel -1 if x_vel > 0 else x_vel + 1 if x_vel < 0 else 0
    y_vel -= 1

    return (x_pos, y_pos), (x_vel, y_vel)


def fire(start_vel):
    current_pos = (0, 0)
    current_vel = start_vel
    max_y = None

    while current_pos[1] >= min(y1, y2):
        (current_pos), current_vel = step(current_pos, current_vel)
        x, y = current_pos
        if max_y is None or max_y < y:
            max_y = y
        if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
            return True, max_y
        elif x > max(x1, x2) and y > max(y1, y2):  # overshot
            return False, True

    return False, False  # probably undershot


def run_simulation(min_y_attempt, max_y_attempt):
    for x in range(max(x1, x2) + 1):
        for y in range(min_y_attempt, max_y_attempt):
            hit, hit_max_y_or_overshot = fire((x, y))
            if hit:
                yield x, y, hit_max_y_or_overshot
            elif hit_max_y_or_overshot:  # Overshot; not point firing harder
                continue


print(f"Part 1: {max(my for _, _, my in run_simulation(0, 1000))}")
print(f"Part 2: {len(set((x, y) for x, y, _ in run_simulation(min(y1, y2), 2000)))}")
