from raw_input import raw_input

SORT_ORDER = {count: priority for priority, count in enumerate([2, 3, 4, 7, 5, 6])}

lines = raw_input.split("\n")

total = 0

for line in lines:
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

    total += int("".join(str(defs[o]) for o in outs))


print(
    "Part 1: "
    + str(
        sum(
            1
            for line in lines
            for output in line.split(" | ")[1].split()
            if len(output) in (2, 4, 3, 7)
        )
    )
)
print(f"Part 2: {total}")
