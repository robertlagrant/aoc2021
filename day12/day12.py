from collections import Counter, defaultdict

from raw_input import raw_input

N = defaultdict(list)
for a, b in [line.split("-") for line in raw_input.split("\n")]:
    N[a].append(b)
    if a != "start" and b != "end":
        N[b].append(a)


def explore(one_small_dupe=False):
    routes, to_process = set(), ["start"]
    while to_process:
        nodes = (route := to_process.pop()).split(",")
        for next_node in [n for n in N[nodes[-1]] if n.isupper() or n not in nodes
                    or (one_small_dupe and all(c == 1 for c in Counter(n for n in nodes if not n.isupper()).values()))]:
            routes.add(new_route := f"{route},{next_node}")
            to_process = to_process + [new_route] if next_node != "end" else to_process

    return routes


print(f"Part 1: {sum(r.endswith('end') for r in explore())}")
print(f"Part 2: {sum(r.endswith('end') for r in explore(one_small_dupe=True))}")
