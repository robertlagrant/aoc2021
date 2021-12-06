from collections import Counter, defaultdict

from raw_input import raw_input


def run_simulation(days: int):
    fish_ages = Counter(raw_input)

    for _ in range(days):
        new_fish_ages = defaultdict(int, {6: fish_ages[0], 8: fish_ages[0]})

        for age, count in fish_ages.items():
            if age != 0:
                new_fish_ages[age-1] += count

        fish_ages = new_fish_ages

    return fish_ages


print(f"Part 1: {sum(count for count in run_simulation(80).values())}")
print(f"Part 2: {sum(count for count in run_simulation(256).values())}")
