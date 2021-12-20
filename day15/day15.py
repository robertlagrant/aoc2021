import networkx as nx

from raw_input import raw

ROWS = [[int(c) for c in r] for r in raw.split("\n")]


def generate_square_map(tile, num_tiles=1):
    side = len(tile)
    return [
        [(n if (n := tile[row_i % side][col_i % side] + (row_i // side) + (col_i // side)) <= 9 else n - 9)
         for col_i in range(side * num_tiles)]
        for row_i in range(side * num_tiles)
    ]


def shortest_route(tile):
    g = nx.DiGraph()
    for row in range((side := len(tile) - 1) + 1):
        for col in range(side + 1):
            if col != side:
                g.add_edge((col + 1, row), (col, row), weight=tile[row][col])
                g.add_edge((col, row), (col + 1, row), weight=tile[row][col + 1])
            if row != side:
                g.add_edge((col, row), (col, row + 1), weight=tile[row + 1][col])
                g.add_edge((col, row + 1), (col, row), weight=tile[row][col])
    return nx.shortest_path_length(g, (0, 0), (side, side), weight="weight")


print(f"Part 1: {shortest_route(generate_square_map(ROWS, 1))}")
print(f"Part 2: {shortest_route(generate_square_map(ROWS, 5))}")
