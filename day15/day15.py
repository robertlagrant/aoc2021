from itertools import pairwise

import networkx as nx

from test_input import raw


def shortest_route(tile, map_edge_size=1):
    g = nx.DiGraph()
    for row in range(len(tile) * map_edge_size):
        for col in range(len(tile[0]) * map_edge_size):
            if col != (len(tile[0]) * map_edge_size) - 1:
                g.add_edge((col + 1, row), (col, row), weight=tile[row % map_edge_size][col % map_edge_size] + map_edge_size - 1)
                g.add_edge((col, row), (col + 1, row), weight=tile[row % map_edge_size][(col + 1) % map_edge_size] + map_edge_size - 1)
            if row != len(tile) * map_edge_size - 1:
                g.add_edge((col, row), (col, row + 1), weight=tile[(row + 1) % map_edge_size][col % map_edge_size] + map_edge_size - 1)
                g.add_edge((col, row + 1), (col, row), weight=tile[row % map_edge_size][col % map_edge_size] + map_edge_size - 1)

    route = nx.shortest_path(g, (0, 0), (len(tile[0] * map_edge_size) - 1, len(tile) * map_edge_size - 1), weight="weight")

    return sum(g.get_edge_data(a, b)["weight"] for a, b in pairwise(route))


ROWS = [[int(c) for c in r] for r in raw.split("\n")]
print(f"Part 1: {shortest_route(ROWS)}")
print(f"Part 2: {shortest_route(ROWS, map_edge_size=5)}")
