from raw_input import raw

dots = [tuple(map(int, row.split(","))) for row in raw[0].split("\n")]
folds = [tuple(row[11:].split("=")) for row in raw[1].split("\n")]

dots_width = max(w for w, h in dots) + 1
dots_height = max(h for w, h in dots) + 1


def ppprint(_dots):
    for row in range(dots_height):
        print("".join("#" if (col, row) in _dots else "." for col in range(dots_width)))


for direction, size in map(lambda f: (f[0], int(f[1])), folds):
    print(direction, size)
    new_dots = set()
    for x, y in dots:


        if direction == "y":
            if y < size:
                new_dots.add((x, y))
            else:
                new_dots.add((x, y - 2 * (y - size)))

            dots_height = size
        elif direction == "x":
            if x < size:
                new_dots.add((x, y))
            else:
                new_dots.add((x - 2 * (x - size), y))

        dots_width = size

    dots_width = size if direction == "x" else dots_width
    dots_height = size if direction == "y" else dots_height
    dots = new_dots
    # ppprint(new_dots)
    # print(len(new_dots))

ppprint(dots)



