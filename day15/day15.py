from itertools import pairwise

import networkx as nx

from test_input import raw

ROWS = [[int(c) for c in r] for r in raw.split("\n")]


def shortest_route(tile, map_edge_size=1):
    width, height = len(tile[0]), len(tile)
    G = nx.DiGraph()
    for i in range(map_edge_size):
        for row in range(height):
            for col in range(width):
                if col != width - 1:
                    G.add_edge((col + 1, row), (col, row), weight=tile[row][col])
                    G.add_edge((col, row), (col + 1, row), weight=tile[row][col + 1])
                if row != height - 1:
                    G.add_edge((col, row), (col, row + 1), weight=tile[row + 1][col])
                    G.add_edge((col, row + 1), (col, row), weight=tile[row][col])

    route = nx.shortest_path(G, (0, 0), (width - 1, height - 1), weight="weight")

    return sum(G.get_edge_data(a, b)["weight"] for a, b in pairwise(route))


print(f"Part 1: {shortest_route(ROWS)}")
