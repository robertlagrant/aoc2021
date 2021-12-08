from raw_input import raw_input

SEGMENT_DEFS = {i: frozenset(s) for i, s in enumerate(["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"])}
SIMPLE_SEGMENT_COUNTS = {2: 1, 3: 7, 4: 4, 7: 8}

lines = raw_input.split('\n')

total = 0
for line in lines:
    ins = [frozenset(word) for word in line.split(" | ")[0].split(" ")]

    # Find 1, 4
    def_1 = [i for i in ins if len(i) == 2][0]
    def_4 = [i for i in ins if len(i) == 4][0]
    bd = def_4 - def_1
    defs = {def_1: 1, def_4: 4}

    for i, lenny in map(lambda x: (x, len(x)), ins):
        if lenny in SIMPLE_SEGMENT_COUNTS.keys():
            defs[i] = SIMPLE_SEGMENT_COUNTS[lenny]

    # Find the rest!
    for i, lenny in map(lambda x: (x, len(x)), ins):
        if lenny == 5:
            if bd.issubset(i):
                defs[i] = 5
            elif def_1.issubset(i):
                defs[i] = 3
            else:
                defs[i] = 2
        elif lenny == 6:
            if not bd.issubset(i):
                defs[i] = 0
            elif def_1.issubset(i):
                defs[i] = 9
            else:
                defs[i] = 6

    total += int("".join(str(defs[o]) for o in [frozenset(word) for word in line.split(" | ")[1].split(" ")]))


print("Part 1: " + str(sum(1 for line in lines for output in line.split(' | ')[1].split() if len(output) in (2, 4, 3, 7))))
print(f"Part 2: {total}")
