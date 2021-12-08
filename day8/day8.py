from raw_input import raw_input

SORT_ORDER = {count: priority for priority, count in enumerate([2, 3, 4, 7, 5, 6])}

lines = raw_input.split("\n")


def parse_line(line):
    ins = [frozenset(word) for word in line.split(" | ")[0].split(" ")]
    outs = [frozenset(word) for word in line.split(" | ")[1].split(" ")]
    ins.sort(key=lambda x: SORT_ORDER[len(x)])
    defs = {ins[x]: y for x, y in zip([0, 1, 2, 3], [1, 7, 4, 8])}
    bd = ins[2] - ins[0]
    for i, lenny in map(lambda x: (x, len(x)), ins):
        if lenny == 5:
            if bd < i:
                defs[i] = 5
            elif ins[0] < i:
                defs[i] = 3
            else:
                defs[i] = 2
        elif lenny == 6:
            if not bd < i:
                defs[i] = 0
            elif ins[0] < i:
                defs[i] = 9
            else:
                defs[i] = 6

    return defs, outs


print(f"Part 1: {sum(1 for line in lines for out in parse_line(line)[1] if len(out) in (2, 4, 3, 7))}")
print(f"Part 2: {sum(int(''.join(str(parse_line(line)[0][o]) for o in parse_line(line)[1])) for line in lines)}")
