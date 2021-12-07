from raw_input import raw_input


def calculate_min_fuel(fuel_rate_modifier):
    return min(
        sum(fuel_rate_modifier(abs(target - crab)) for crab in raw_input)
        for target in range(min(raw_input), max(raw_input) + 1))


print(f"Part 1: {calculate_min_fuel(fuel_rate_modifier=lambda x: x)}")
print(f"Part 2: {calculate_min_fuel(fuel_rate_modifier=lambda x: int(x*(x+1)/2))}")
