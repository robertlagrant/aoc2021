from functools import reduce

from raw_input import algo, image


PADDING = 1000


def surround(im: str):
    rows = im.split("\n")
    return "\n".join([
        *[r for r in ["0" * (2 * PADDING + len(rows))] * PADDING],
        *["0" * PADDING + f"{''.join(['0' if c in '.0' else '1' for c in r])}" + "0" * PADDING for r in rows],
        *[r for r in ["0" * (2 * PADDING + len(rows))] * PADDING],
    ])


def enhance(im, round):
    print(round)
    _im = ["".join("0" if c in ".0" else "1" for c in row) for row in im.split("\n")]

    out = []
    for i in range(1, len(_im) - 1):
        row = ""
        for j in range(1, len(_im[0]) - 1):
            lookup = int("".join([_im[i+d_x][j - 1:j + 2] for d_x in (-1, 0, 1)]), 2)
            row += algo[lookup]
        out.append(row)

    return "\n".join(out)


print(f"Part 1: {sum(c == '#' for c in reduce(lambda im, x: enhance(im, x+1), range(2), surround(image)))}")
print(f"Part 2: {sum(c == '#' for c in reduce(lambda im, x: enhance(im, x+1), range(50), surround(image)))}")
