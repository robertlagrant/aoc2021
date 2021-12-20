import networkx as nx

from raw_input import raw


def generate_square_map(tile, num_tiles=1):
    side = len(tile)
    return [
        [(n if (n := tile[r_i % side][c_i % side] + (r_i // side) + (c_i // side)) <= 9 else n - 9)
         for c_i in range(side * num_tiles)]
        for r_i in range(side * num_tiles)
    ]


def shortest_route(t):
    g = nx.DiGraph()
    for r in range(side := len(t)):
        for c in range(side):
            if c != side - 1:
                g.add_edges_from([((c + 1, r), (c, r), {"w": t[r][c]}), ((c, r), (c + 1, r), {"w": t[r][c + 1]})])
            if r != side - 1:
                g.add_edges_from([((c, r), (c, r + 1), {"w": t[r + 1][c]}), ((c, r + 1), (c, r), {"w": t[r][c]})])
    return nx.shortest_path_length(g, (0, 0), (side - 1, side - 1), weight="w")


ROWS = [[int(c) for c in r] for r in raw.split("\n")]
print(f"Part 1: {shortest_route(generate_square_map(ROWS))}")
print(f"Part 2: {shortest_route(generate_square_map(ROWS, num_tiles=5))}")
