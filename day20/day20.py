from raw_input import algo, image


def surround(im):
    rows = im.split("\n")
    return [(new_r := "0" * (2 + len(rows))), *[f"0{''.join(['0' if c in '.0' else '1' for c in r])}0" for r in rows], new_r]


def enhance(im, do_surround=True):
    if do_surround:
        _im = surround("\n".join(surround("\n".join(surround("\n".join(surround("\n".join(surround("\n".join(surround("\n".join(surround("\n".join(surround("\n".join(surround("\n".join(surround("\n".join(surround(im)))))))))))))))))))))
    else:
        _im = ["".join("0" if c in ".0" else "1" for c in row) for row in im.split("\n")]
    # print("\n".join(_im))
    # print()
    out = []
    for i in range(1, len(_im) - 1):
        row = ""
        for j in range(1, len(_im[0]) - 1):
            lookup = int("".join([_im[i+d_x][j - 1:j + 2] for d_x in (-1, 0, 1)]), 2)
            row += algo[lookup]
        out.append(row)
    # print("\n".join(out))
    # print()
    return "\n".join(out)


print(f"Part 1: {sum(c == '#' for row in enhance(enhance(image), do_surround=False) for c in row)}")
# print(f"Part 2: {reduce()}")
