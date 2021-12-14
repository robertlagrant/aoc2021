from collections import Counter
from functools import cache, reduce

from raw_input import raw

HULL = raw[0]
RULES = {a: a[0] + b + a[1] for a, b in (tuple(rr.split(" -> ")) for rr in raw[1].split("\n"))}


@cache
def expand(_in: str, iterations: int, rules) -> Counter:
    if not iterations or (len(_in) == 2 and _in not in rules):
        return Counter(_in[:-1])

    if _in in rules:
        _in = rules[_in]
        iterations -= 1

    return reduce(lambda c1, c2: c1 + c2, [expand(_in[j:j+2], iterations) for j in range(len(_in) - 1)])


print(f"Part 1: {(c := [b for a, b in (expand(HULL, 10, RULES) + Counter([HULL[-1]])).most_common()])[0] - c[-1]}")
print(f"Part 2: {(c := [b for a, b in (expand(HULL, 40, RULES) + Counter([HULL[-1]])).most_common()])[0] - c[-1]}")
