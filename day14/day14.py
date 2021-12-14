from collections import Counter, deque

from test_input import raw

hull = deque(raw[0])
rules = {a: b for a, b in (tuple(rr.split(" -> ")) for rr in raw[1].split("\n"))}
print(rules)

for i in range(40):
    # print("".join(hull))
    pointer = 0
    while pointer < len(hull) - 1:
        if (matched_polymer := hull[pointer] + hull[pointer+1]) in rules:
            hull.insert(pointer + 1, rules[matched_polymer])
            pointer += 1
        pointer += 1

# print("".join(hull))
print(c := [b for a, b in Counter(hull).most_common()])
print(c[0] - c[-1])
