from raw_input import raw_input

lines = raw_input.split("\n")


def process_line(line, f):
    ins, outs = map(lambda i: [frozenset(word) for word in line.split(" | ")[i].split(" ")], [0, 1])
    ins.sort(key=lambda x: {c: p for p, c in enumerate([2, 3, 4, 7, 5, 6])}[len(x)])

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

    return f(defs, outs)


print(f"Part 1: {sum(process_line(l, lambda _, outs: sum(1 for o in outs if len(o) in (2, 4, 3, 7))) for l in lines)}")
print(f"Part 2: {sum(process_line(l, lambda defs, outs: int(''.join(str(defs[o]) for o in outs)) ) for l in lines)}")

