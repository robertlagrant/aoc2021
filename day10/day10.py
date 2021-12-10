from functools import reduce

from raw_input import raw_input

PAIRS, RPAIRS = [{cs[a]: cs[b] for cs in ["()", "[]", "{}", "<>"]} for a, b in [(1, 0), (0, 1)]]
SCORES = {")": (3, 1), "]": (57, 2), "}": (1197, 3), ">": (25137, 4)}


def analyse_line(_line, mode):
    curr = ""
    for c in _line:
        if c in PAIRS.keys() and curr[-1] != PAIRS[c]:
            return SCORES[c][0] if mode == 1 else None
        curr = curr + c if c in PAIRS.values() else curr[:-1]

    return reduce(lambda x, y: x * 5 + y, (SCORES[RPAIRS[c]][1] for c in curr[::-1]), 0) if curr and mode == 2 else None


lines = raw_input.split("\n")
print(f"Part 1: {sum(a for l in lines if (a := analyse_line(l, mode=1)))}")
print(f"Part 2: {sorted(scores := [a for l in lines if (a := analyse_line(l, mode=2))])[len(scores)//2]}")
