import re
from functools import reduce
from itertools import combinations

from raw_input import raw


def explode(s):
    i, depth, exploded = 0, 0, False
    while i < len(s) and not exploded:
        inc = 1
        if m := re.match(r"\[(?P<n1>\d+),(?P<n2>\d+)]", s[i:]):
            if exploded := depth >= 4:  # explode
                s = s[:i] + "0" + s[i + m.end():]  # snip out the exploded bit, replace with "0"
                if n1_m := re.findall(r"(\d+)", s[:i]):  # Search back to find a place for the left num, else discard
                    prev_len = len(s)
                    s = s[:(r := s[:i].rfind(n := n1_m[-1]))] + str(int(n) + int(m.groupdict()["n1"])) + s[r + len(n):]
                    i += len(s) - prev_len

                i += 1  # Skip the 0
                if n2_m := re.search(r"(\d+)", s[i:]):  # Search forward to find a place for the right num, else discard
                    s = s[:i] + s[i:].replace((n := n2_m.groups()[0]), str(int(n) + int(m.groupdict()["n2"])), 1)
            else:
                inc = m.end()  # skip past the simple match
        elif s[i] == "[":
            depth += 1
        elif s[i] == "]":
            depth -= 1
        i += inc
    return s


def split(s):
    if m := re.search(r"(\d\d+)", s):
        return f"{s[0:m.start()]}[{(val := int(m.groups()[0]))//2},{(val+1)//2}]{s[m.end():]}"
    return s


def reduct(s):
    while True:
        if s == (maybe_exploded := explode(s)) == (maybe_split := split(s)):
            return s
        s = maybe_exploded if maybe_exploded != s else maybe_split


def add(s1, s2):
    return reduct(f"[{s1},{s2}]")


def magnitude(pair):
    return 3 * (pair[0] if isinstance(pair[0], int) else magnitude(pair[0])) \
        + 2 * (pair[1] if isinstance(pair[1], int) else magnitude(pair[1]))


print(f"Part 1: " + str(magnitude(eval(reduce(add, raw.split("\n"))))))
print(f"Part 2: " + str(max(magnitude(eval(add(a, b))) for a, b in combinations(raw.split("\n"), 2))))
