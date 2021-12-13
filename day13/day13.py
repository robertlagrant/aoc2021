from raw_input import raw

dots = [tuple(map(int, row.split(","))) for row in raw[0].split("\n")]
folds = [tuple(row[11:].split("=")) for row in raw[1].split("\n")]


def run_dots(_dots, iterations=None):
    dots_w = max(w for w, _ in dots) + 1
    dots_h = max(h for _, h in dots) + 1
    for direction, size in map(lambda f: (f[0], int(f[1])), folds):
        dots_w = size if direction == "x" else dots_w
        dots_h = size if direction == "y" else dots_h
        _dots = set(
            (x, y - 2 * (y - size)) if direction == "y" and y >= size
            else (x - 2 * (x - size), y) if direction == "x" and x >= size
            else (x, y)
            for x, y in _dots
        )
        if iterations is not None and (iterations := iterations - 1) == 0:
            break
    return "\n".join("".join("#" if (col, row) in _dots else "." for col in range(dots_w)) for row in range(dots_h))


print(f"Part 1: {sum([c == '#' for _dots in run_dots(dots, iterations=1) for c in _dots])}")
print(f"Part 2: \n{run_dots(dots)}")
