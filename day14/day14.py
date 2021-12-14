from collections import Counter
from functools import cache

from test_input import raw

hull = raw[0]
rules = {a: a[0] + b + a[1] for a, b in (tuple(rr.split(" -> ")) for rr in raw[1].split("\n"))}


@cache
def expand(_in, iterations):
    if iterations == 0:
        return _in

    if len(_in) == 2:
        # print("Length is 2!")
        _in = rules[_in] if _in in rules else _in
        return expand(_in, iterations - 1) if len(_in) > 2 else _in

    _next = []
    for j in range(len(_in) - 1):
        _next.append(expand(_in[j:j+2], iterations)[:-1])

    _in = "".join(_next) + _in[-1]

    return _in


its = 40
new_hull = expand(hull, its)
print(new_hull)
print((c := [b for a, b in Counter(new_hull).most_common()])[0] - c[-1])
