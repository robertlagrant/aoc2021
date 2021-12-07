from raw_input import raw_input


def calculate_min_fuel(cost_function):
    return min(
        sum(cost_function(abs(target - crab)) for crab in raw_input)
        for target in range(min(raw_input), max(raw_input) + 1))


print(f"Part 1: {calculate_min_fuel(lambda x: x)}")
print(f"Part 2: {calculate_min_fuel(lambda x: int(x*(x+1)/2))}")
