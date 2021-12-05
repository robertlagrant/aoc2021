from collections import defaultdict

from raw_input import raw_input, test_input

data = raw_input.split()

data_len = len(data)
data_width = len(data[0])
ones_counts = defaultdict(int)

for d in data:
    for i, c in enumerate(d):
        if c == "1":
            ones_counts[i] += 1

gamma = int("".join("1" if (ones_counts[i] > data_len/2) else "0" for i in range(data_width)), 2)
epsilon = int("".join("1" if (ones_counts[i] < data_len/2) else "0" for i in range(data_width)), 2)


def filter_nums(nums: [str], aim_high: bool, so_far="") -> [str]:
    if len(nums) == 1:
        return nums

    index = len(so_far)
    ones = [num for num in nums if num[index] == "1"]
    zeros = [num for num in nums if num[index] == "0"]

    if aim_high:
        new_nums = zeros if len(ones) < len(zeros) else ones
        so_far += "0" if len(ones) < len(zeros) else "1"
    else:
        new_nums = ones if len(ones) < len(zeros) else zeros
        so_far += "1" if len(ones) < len(zeros) else "0"

    return filter_nums(new_nums, aim_high, so_far)


o2_generator_rating = int(filter_nums(data, aim_high=True)[0], 2)
co2_scrubber_rating = int(filter_nums(data, aim_high=False)[0], 2)

print(f"Part 1: {gamma * epsilon}")
print(f"Part 2: {o2_generator_rating * co2_scrubber_rating}")
