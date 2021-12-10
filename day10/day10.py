from functools import reduce

from raw_input import raw_input

lines = raw_input.split("\n")

BAROQUE_INFO = [("()", 3, 1), ("[]", 57, 2), ("{}", 1197, 3), ("<>", 25137, 4)]

PAIRS = {(b := list(info[0]))[1]: b[0] for info in BAROQUE_INFO}
RPAIRS = {(b := list(info[0]))[0]: b[1] for info in BAROQUE_INFO}
SEVERITY = {list(info[0])[1]: info[1] for info in BAROQUE_INFO}
SCORES = {list(info[0])[1]: info[2] for info in BAROQUE_INFO}


def analyse_line(_line, _type=1):
    current_open = ""
    line_corrupt = False
    for c in _line:
        if c in PAIRS.values():
            current_open += c
        elif c in PAIRS.keys():
            if current_open[-1] != PAIRS[c]:
                line_corrupt = True
                if _type == 1:
                    return 1, SEVERITY[c]
            current_open = current_open[:-1]

    if not line_corrupt and len(current_open) and _type == 2:
        return reduce(lambda x, y: (x * 5) + SCORES[y], "".join(RPAIRS[c] for c in reversed(current_open)), 0)

    return None


print(f"Part 1: {sum(s for r, s in [analyse_line(l) for l in lines if analyse_line(l) is not None] if r == 1)}")
print(f"Part 2: {sorted(scores := [a for l in lines if (a := analyse_line(l, _type=2))])[len(scores)//2]}")
