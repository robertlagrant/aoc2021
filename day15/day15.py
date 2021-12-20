import networkx as nx

from raw_input import raw

ROWS = [[int(c) for c in r] for r in raw.split("\n")]


def generate_square_map(tile, edge_tiles_count=1):
    rows = []
    for row_index in range((tile_edge_len := len(tile)) * edge_tiles_count):
        row = []
        for col_index in range(tile_edge_len * edge_tiles_count):
            row.append(n if (n := tile[row_index % tile_edge_len][col_index % tile_edge_len]
                             + (row_index // tile_edge_len)
                             + (col_index // tile_edge_len)) <= 9 else n-9)
        rows.append("".join(map(str, row)))
    return rows


def shortest_route(tile):
    g = nx.DiGraph()
    for row in range((side := len(tile) - 1) + 1):
        for col in range(side + 1):
            if col != side:
                g.add_edge((col + 1, row), (col, row), weight=int(tile[row][col]))
                g.add_edge((col, row), (col + 1, row), weight=int(tile[row][col + 1]))
            if row != side:
                g.add_edge((col, row), (col, row + 1), weight=int(tile[row + 1][col]))
                g.add_edge((col, row + 1), (col, row), weight=int(tile[row][col]))
    return nx.shortest_path_length(g, (0, 0), (side, side), weight="weight")


print(f"Part 1: {shortest_route(ROWS)}")
print(f"Part 2: {shortest_route(generate_square_map(ROWS, 5))}")
