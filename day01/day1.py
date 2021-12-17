# raw_input is just the input text as a string
from raw_input import raw_input

nums = [int(s) for s in raw_input.split()]
print(f"Part 1: {sum(1 for i in range(len(nums)-1) if nums[i] < nums[i+1])}")
print(f"Part 2: {sum(1 for i in range(len(nums)-3) if nums[i] < nums[i+3])}")
