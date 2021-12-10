from raw_input import raw_input

lines = raw_input.split("\n")

BRACKETS = [("()", 3, 1), ("[]", 57, 2), ("{}", 1197, 3), ("<>", 25137, 4)]

PAIRS = {(b := list(bracket[0]))[1]: b[0] for bracket in BRACKETS}
RPAIRS = {(b := list(bracket[0]))[0]: b[1] for bracket in BRACKETS}
SEVERITY = {list(bracket[0])[1]: bracket[1] for bracket in BRACKETS}
SCORES = {list(bracket[0])[1]: bracket[2] for bracket in BRACKETS}


def analyse_line(_line):
    current_open = ""
    for c in _line:
        if c in PAIRS.values():
            current_open += c
        elif c in PAIRS.keys():
            if current_open[-1] != PAIRS[c]:
                return 1, SEVERITY[c]
            current_open = current_open[:-1]

    if len(current_open):
        missing = "".join(RPAIRS[c] for c in reversed(current_open))
        _score = 0
        for c in missing:
            _score *= 5
            _score += SCORES[c]
        return 2, _score

    return 0, None


corrupt_score = 0
for line in lines:
    result, score = analyse_line(line)
    if result == 1:
        corrupt_score += score

print(f"Part 1: {corrupt_score}")

scores = []
for line in lines:
    result, score = analyse_line(line)
    if result == 2:
        scores.append(score)

print(f"Part 2: {sorted(scores)[len(scores)//2]}")
