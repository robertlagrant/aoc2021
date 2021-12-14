from collections import Counter, deque

from raw_input import raw

hull = deque(raw[0])
rules = {a: b for a, b in (tuple(rr.split(" -> ")) for rr in raw[1].split("\n"))}

for i in range(40):
    print(f"Step {i}")
    for _ in range(len(hull) - 1):
        if (matched_polymer := hull[0] + hull[1]) in rules:
            hull.insert(1, rules[matched_polymer])
            hull.rotate(-1)
        hull.rotate(-1)
    hull.rotate(-1)

print((c := [b for a, b in Counter(hull).most_common()])[0] - c[-1])
