from test_input import raw


class Node:
    def __init__(self, raw_node):
        self.left = raw_node[0] if type(raw_node[0]) == int else Node(raw_node[0])
        self.right = raw_node[1] if type(raw_node[1]) == int else Node(raw_node[1])

    def __repr__(self):
        return f"Node({self.left}, {self.right})"


for line in raw.split("\n"):
    root = Node(eval(line))

    print(line, root)