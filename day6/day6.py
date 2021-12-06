from collections import Counter

from raw_input import raw_input


def count_ages(days: int, start_model):
    c = Counter(start_model)

    for _ in range(days):
        c = {0: c[1], 1: c[2], 2: c[3], 3: c[4], 4: c[5], 5: c[6], 6: c[7] + c[0], 7: c[8], 8: c[0]}

    return c


print(f"Part 1: {sum(count for count in count_ages(80, start_model=raw_input).values())}")
print(f"Part 2: {sum(count for count in count_ages(256, start_model=raw_input).values())}")
