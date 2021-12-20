from itertools import pairwise
# import matplotlib.pyplot as plt
import networkx as nx

from raw_input import raw

# raw = """123
# 456
# 789"""

ROWS = [[int(c) for c in r] for r in raw.split("\n")]


def generate_square_map(tile, edge_tiles_count=1):
    tile_edge_len = len(tile)
    rows = []
    for row_index in range(tile_edge_len * edge_tiles_count):  # 0..29
        row = []
        for col_index in range(tile_edge_len * edge_tiles_count):  # 0..29
            num = tile[row_index % tile_edge_len][col_index % tile_edge_len] \
                + (row_index // tile_edge_len) \
                + (col_index // tile_edge_len)
            while num > 9:
                num -= 9
            row.append(
                num
            )
        rows.append("".join(map(str, row)))
    return rows


def shortest_route(tile):
    width, height = len(tile[0]), len(tile)
    g = nx.DiGraph()

    for row in range(height):
        for col in range(width):
            if col != width - 1:
                g.add_edge((col + 1, row), (col, row), weight=int(tile[row][col]))
                g.add_edge((col, row), (col + 1, row), weight=int(tile[row][col + 1]))
            if row != height - 1:
                g.add_edge((col, row), (col, row + 1), weight=int(tile[row + 1][col]))
                g.add_edge((col, row + 1), (col, row), weight=int(tile[row][col]))

    # print(len(g.nodes), len(g.edges))
    #
    # nx.draw_networkx(g, with_labels=True, font_weight='bold')
    # plt.savefig("path.png")
    #
    # print(g.edges)

    route = nx.shortest_path(g, (0, 0), (width - 1, height - 1), weight="weight")

    return sum(g.get_edge_data(a, b)["weight"] for a, b in pairwise(route))


print(f"Part 1: {shortest_route(ROWS)}")
print(f"Part 2: {shortest_route(generate_square_map(ROWS, 5))}")


