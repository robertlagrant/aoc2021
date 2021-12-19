import re
from functools import reduce
from itertools import combinations

from raw_input import raw

SIMPLE_MATCH = r"\[(?P<n1>\d+),(?P<n2>\d+)\]"


def explode(s):
    i, depth, exploded = 0, 0, False
    while i < len(s) and not exploded:
        inc = 1
        if m := re.match(SIMPLE_MATCH, s[i:]):
            if depth >= 4:  # explode
                exploded = True
                s = s[:i] + "0" + s[i + m.end():]  # snip out the exploded bit, replace with "0"
                prev_len, new_len = 0, 0

                # Search back to find a place for the left num, otherwise discard
                if n1_m := re.findall(r"(\d+)", s[:i]):
                    found_num1 = n1_m[-1]
                    new_num = int(found_num1) + int(m.groupdict()["n1"])
                    prev_len = len(s)
                    s = s[:s[:i].rfind(found_num1)] + str(new_num) + s[s[:i].rfind(found_num1) + len(found_num1):]
                    new_len = len(s)

                # Skip the zero
                i += 1 + new_len - prev_len

                # Search forward to find a place for the right num, otherwise discard
                if n2_m := re.search(r"(\d+)", s[i:]):
                    found_num2 = n2_m.groups()[0]

                    new_num = int(found_num2) + int(m.groupdict()["n2"])
                    s = s[:i] + s[i:].replace(found_num2, str(new_num), 1)
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
        # print("SPLIT!")
        low = int(m.groups()[0])//2
        high = (int(m.groups()[0])+1)//2
        return f"{s[0:m.start()]}[{low},{high}]{s[m.end():]}"
    return s


def reduct(s):
    cont = True
    while cont:
        maybe_exploded = explode(s)
        if s != maybe_exploded:
            s = maybe_exploded
        else:
            maybe_split = split(s)
            if s != maybe_split:
                s = maybe_split
            else:
                cont = False
    return s


def add(s1, s2):
    return reduct(f"[{s1},{s2}]")


def magnitude(pair):
    left, right = pair
    if not isinstance(left, int):
        left = magnitude(left)
    if not isinstance(right, int):
        right = magnitude(right)

    return 3 * left + 2 * right


print(f"Part 1: " + str(magnitude(eval(reduce(add, raw.split("\n"))))))
print(f"Part 2: " + str(max(magnitude(eval(add(a, b))) for a, b in combinations(raw.split("\n"), 2))))
