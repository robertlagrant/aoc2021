import re
from functools import reduce

from raw_input import raw

SIMPLE_MATCH = r"\[(?P<n1>\d+),(?P<n2>\d+)\]"


def explode(s):
    i, depth, exploded = 0, 0, False
    while i < len(s) and not exploded:
        # print(raw, raw[i:])
        inc = 1
        if m := re.match(SIMPLE_MATCH, s[i:]):
            if depth >= 4:  # explode
                exploded = True
                # print("EXPLODE!")
                s = s[:i] + "0" + s[i + m.end():]  # snip out the exploded bit, replace with "0"
                prev_len, new_len = 0, 0

                # Search back to find a place for the left num, otherwise discard
                # print(f"Left - looking in {s[:i]}")
                if n1_m := re.findall(r"(\d+)", s[:i]):
                    # print(f"Found it here! {n1_m[-1]}")
                    found_num1 = n1_m[-1]
                    new_num = int(found_num1) + int(m.groupdict()["n1"])
                    prev_len = len(s)
                    s = s[:s[:i].rfind(found_num1)] + str(new_num) + s[s[:i].rfind(found_num1) + len(found_num1):]
                    new_len = len(s)
                    # print(f"All done!")
                    # print(s)
                # else:
                #     print("Nowhere for explode left")

                # print("")

                # Skip the zero
                i += 1 + new_len - prev_len

                # Search forward to find a place for the right num, otherwise discard
                # print(f"Searching for right in {raw[i:]}")
                if n2_m := re.search(r"(\d+)", s[i:]):
                    # print(f"found it here {s[i:]}")
                    found_num2 = n2_m.groups()[0]
                    # print(n2_m.groups())
                    # print("Right: adding to " + found_num2)
                    new_num = int(found_num2) + int(m.groupdict()["n2"])
                    s = s[:i] + s[i:].replace(found_num2, str(new_num), 1)
                # else:
                #     print("Nowhere for explode right")
            else:
                inc = m.end()  # skip past the simple match
        elif s[i] == "[":
            depth += 1
        elif s[i] == "]":
            depth -= 1

        i += inc

    return s


def split(s):
    if m := re.search(r"(\d\d+)", s):
        # print("SPLIT!")
        low = int(m.groups()[0])//2
        high = (int(m.groups()[0])+1)//2
        return f"{s[0:m.start()]}[{low},{high}]{s[m.end():]}"
    return s


# for _in, expected in [
#     ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
#     ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
#     ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
#     ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
#     ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]")
#     ]:
#     print(explode(_in) == expected, _in, expected, explode(_in))
#
# print(x := split("[[[[0,7],4],[15,[0,13]]],[1,1]]"))
# print("[[[[0,7],4],[[7,8],[0,13]]],[1,1]]")
# print(x == "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]")


def reduct(s):
    cont = True
    while cont:
        maybe_exploded = explode(s)
        if s != maybe_exploded:
            s = maybe_exploded
        else:
            maybe_split = split(s)
            if s != maybe_split:
                s = maybe_split
            else:
                cont = False
    return s


def add(s1, s2):
    return reduct(f"[{s1},{s2}]")


def magnitude(pair):
    left, right = pair
    if not isinstance(left, int):
        left = magnitude(left)
    if not isinstance(right, int):
        right = magnitude(right)

    return 3 * left + 2 * right

# test = r"[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
#
# print(reduct(test))
# print(r"[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")

# raw = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
# [[[5,[2,8]],4],[5,[[9,9],0]]]
# [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
# [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
# [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
# [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
# [[[[5,4],[7,7]],8],[[8,3],8]]
# [[9,3],[[9,9],[6,[4,9]]]]
# [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
#
# result = "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"


print(f"Part 1: " + str(magnitude(eval(reduce(add, raw.split("\n"))))))
