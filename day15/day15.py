import networkx as nx

from raw_input import raw


def generate_square_map(tile, num_tiles=1):
    side = len(tile)
    return [
        [(n if (n := tile[r_i % side][c_i % side] + (r_i // side) + (c_i // side)) <= 9 else n - 9)
         for c_i in range(side * num_tiles)]
        for r_i in range(side * num_tiles)
    ]


def shortest_route(tile):
    g = nx.DiGraph()
    for r in range(side := len(tile)):
        for c in range(side):
            if c != side - 1:
                g.add_edge((c + 1, r), (c, r), weight=tile[r][c])
                g.add_edge((c, r), (c + 1, r), weight=tile[r][c + 1])
            if r != side - 1:
                g.add_edge((c, r), (c, r + 1), weight=tile[r + 1][c])
                g.add_edge((c, r + 1), (c, r), weight=tile[r][c])
    return nx.shortest_path_length(g, (0, 0), (side - 1, side - 1), weight="weight")


ROWS = [[int(c) for c in r] for r in raw.split("\n")]
print(f"Part 1: {shortest_route(generate_square_map(ROWS))}")
print(f"Part 2: {shortest_route(generate_square_map(ROWS, num_tiles=5))}")
