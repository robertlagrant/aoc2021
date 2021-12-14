from collections import Counter
from functools import cache

from raw_input import raw

hull = raw[0]
rules = {a: a[0] + b + a[1] for a, b in (tuple(rr.split(" -> ")) for rr in raw[1].split("\n"))}

its = 40


@cache
def expand(_in, iterations) -> Counter:
    if iterations == 0:
        return Counter(_in[:-1])

    if len(_in) == 2:
        _in = rules[_in] if _in in rules else _in
        iterations -= 1

    c = Counter()
    for j in range(len(_in) - 1):
        c2 = expand(_in[j:j+2], iterations)
        c += c2

    return c


new_hull = expand(hull, its) + Counter([hull[-1]])
print(new_hull)
print((c := [b for a, b in Counter(new_hull).most_common()])[0] - c[-1])
