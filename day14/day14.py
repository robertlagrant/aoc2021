from collections import Counter
from functools import cache, reduce
from itertools import pairwise

from raw_input import raw

HULL = raw[0]
RULES = {a: a[0] + b + a[1] for a, b in [rr.split(" -> ") for rr in raw[1].split("\n")]}


@cache
def expand(_in: str, its: int) -> Counter:
    if its == 0 or len(_in) == 2 and _in not in RULES:
        return Counter(_in[-1])

    if _in in RULES:
        _in = RULES[_in]
        its -= 1

    return reduce(
        lambda c, d: c + d,
        [expand(_in[j:j+2], its) for j in range(len(_in) - 1)]
    )


print(f"Part 1: {(c := [b for _, b in (expand(HULL, 10) + Counter(HULL[-1])).most_common()])[0] - c[-1]}")
print(f"Part 2: {(c := [b for _, b in (expand(HULL, 40) + Counter(HULL[-1])).most_common()])[0] - c[-1]}")
