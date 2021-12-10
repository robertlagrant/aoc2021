from functools import reduce

from raw_input import raw_input

BAROQUE_INFO = [("()", 3, 1), ("[]", 57, 2), ("{}", 1197, 3), ("<>", 25137, 4)]
PAIRS = {tokens[1]: tokens[0] for tokens, _, _ in BAROQUE_INFO}
RPAIRS = {b: a for a, b in PAIRS.items()}
SEVERITY = {tokens[1]: score1 for tokens, score1, _ in BAROQUE_INFO}
SCORES = {tokens[1]: score2 for tokens, _, score2 in BAROQUE_INFO}


def analyse_line(_line, _type):
    current_open = ""
    line_corrupt = False
    for c in _line:
        if c in PAIRS.values():
            current_open += c
        elif c in PAIRS.keys():
            if current_open[-1] != PAIRS[c]:
                line_corrupt = True
                if _type == 1:
                    return SEVERITY[c]
            current_open = current_open[:-1]

    if not line_corrupt and len(current_open) and _type == 2:
        return reduce(lambda x, y: (x * 5) + SCORES[y], "".join(RPAIRS[c] for c in reversed(current_open)), 0)


lines = raw_input.split("\n")
print(f"Part 1: {sum(a for l in lines if (a := analyse_line(l, _type=1)))}")
print(f"Part 2: {sorted(scores := [a for l in lines if (a := analyse_line(l, _type=2))])[len(scores)//2]}")
