import re

from test_input import raw


SIMPLE_MATCH = r"\[(?P<n1>\d+),(?P<n2>\d+)\]"
needs_rerun = True
while needs_rerun:
    print(raw)
    needs_rerun = False
    i = 0
    counter = 0
    while i < len(raw):
        inc = 1
        if m := re.match(SIMPLE_MATCH, raw[i:]):
            if counter >= 4:
                ...  # explode
            else:
                inc = m.end()  # skip past the simple match
            # elif int(m.groupdict()["n1"]) > 9:
            #     ...  # split left
            # elif int(m.groupdict()["n2"]) > 9:
            #     ...  # split right
        elif raw[i] == "[":
            counter += 1
        elif raw[i] == "]":
            counter -= 1

        i += inc


