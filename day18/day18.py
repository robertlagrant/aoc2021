from typing import Tuple

from test_input import raw




class Node:
    left = None
    right = None

    def __repr__(self):
        return f"({str(self.left)}, {str(self.right)})"


def parse(s) -> Tuple[Node, str]:
    if s[0] == "[":
        # print("1", s)
        n = Node()
        if s[1] == "]":
            # print("2", s)
            return n, s[2:]
        elif s[1] == "[":
            # print("3", s)
            n.left, s = parse(s[1:])
            if s.startswith(",["):
                # print("4", s)
                n.right, s = parse(s[1:])
            else:
                # print("5", s)
                n.right, s = s[1:].split("]", 1)
        else:
            # print("6", s)
            n.left, s = s[1:].split(",", 1)
            if s.startswith(",["):
                # print("7", s)
                n.right, s = parse(s[1:])
            else:
                # print("8", s)
                n.right, s = s.split("]", 1)

    return n, s


for line in raw.split("\n"):
    print(line, eval(line))
