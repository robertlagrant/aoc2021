from raw_input import raw_input

commands = [tuple(line.split()) for line in raw_input.split("\n")]

x = 0
y = 0

for d, m_s in commands:
    m = int(m_s)
    if d == "down":
        y += m
    if d == "up":
        y -= m
    if d == "forward":
        x += m

print(f"Part 1: {x*y}")

x = 0
y = 0
a = 0

for d, m_s in commands:
    m = int(m_s)
    if d == "down":
        a += m
    if d == "up":
        a -= m
    if d == "forward":
        x += m
        y += a * m

print(f"Part 2: {x*y}")
