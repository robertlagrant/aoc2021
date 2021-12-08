from raw_input import raw_input

lines = raw_input.split("\n")


def process_line(line, f):
    ins, outs = map(lambda x: [frozenset(word) for word in line.split(" | ")[x].split(" ")], [0, 1])
    ins.sort(key=lambda x: {int(c): p for p, c in enumerate("234756")}[len(x)])

    defs = {ins[int(x)]: int(y) for x, y in zip("0123", "1748")}
    bd = ins[2] - ins[0]
    for i, lenny in map(lambda x: (x, len(x)), ins):
        if lenny == 5:
            defs[i] = 5 if bd < i else 3 if ins[0] < i else 2
        elif lenny == 6:
            defs[i] = 0 if not bd < i else 9 if ins[0] < i else 6

    return f(defs, outs)


print(f"Part 1: {sum(process_line(l, lambda _, outs: sum(1 for o in outs if len(o) in (2, 4, 3, 7))) for l in lines)}")
print(f"Part 2: {sum(process_line(l, lambda defs, outs: int(''.join(str(defs[o]) for o in outs)) ) for l in lines)}")
