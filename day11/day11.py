from itertools import product

from raw_input import raw_input

data = [[int(c) for c in r] for r in raw_input.split("\n")]

WIDTH, HEIGHT = len(data[0]), len(data)
FLASH_COUNT_ITERATION = 100
flash_count, flash_step = 0, None
i = 0

while i <= FLASH_COUNT_ITERATION or flash_step is None:
    i += 1
    to_process = list(product(range(WIDTH), range(HEIGHT)))

    while to_process:
        x, y = to_process.pop()
        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            data[y][x] += 1
            if data[y][x] == 10:
                for _x, _y in [(x + dx, y + dy) for dx, dy in set(product(*[[1, 0, -1]] * 2)) - {(0, 0)}]:
                    to_process.append((_x, _y))

    this_flash_count = sum(_col > 9 for _row in data for _col in _row)
    flash_count += this_flash_count if i <= FLASH_COUNT_ITERATION else 0
    flash_step = i if this_flash_count == WIDTH * HEIGHT and flash_step is None else None

    data = [[0 if data[_y][_x] > 9 else data[_y][_x] for _x in range(WIDTH)] for _y in range(HEIGHT)]

print(f"Part 1: {flash_count}")
print(f"Part 2: {flash_step}")
