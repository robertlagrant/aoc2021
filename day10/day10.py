from functools import reduce

from raw_input import raw_input

BAROQUE_INFO = [("()", 3, 1), ("[]", 57, 2), ("{}", 1197, 3), ("<>", 25137, 4)]
PAIRS = {tokens[1]: tokens[0] for tokens, _, _ in BAROQUE_INFO}
RPAIRS = {b: a for a, b in PAIRS.items()}
SCORES = {tokens[1]: (score1, score2) for tokens, score1, score2 in BAROQUE_INFO}


def analyse_line(_line, _type):
    current, corrupt = "", False
    for c in _line:
        if (corrupt := corrupt or (c in PAIRS.keys() and current[-1] != PAIRS[c])) and _type == 1:
            return SCORES[c][0]
        current = current + c if c in PAIRS.values() else current[:-1]

    if not corrupt and current and _type == 2:
        return reduce(lambda x, y: (x * 5) + SCORES[y][1], "".join(RPAIRS[c] for c in reversed(current)), 0)


lines = raw_input.split("\n")
print(f"Part 1: {sum(a for l in lines if (a := analyse_line(l, _type=1)))}")
print(f"Part 2: {sorted(scores := [a for l in lines if (a := analyse_line(l, _type=2))])[len(scores)//2]}")
