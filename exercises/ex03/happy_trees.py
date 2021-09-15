"""Drawing forests in a loop."""

__author__ = "730396074"

TREE: str = '\U0001F332'
i = int(input("Depth: "))
s = TREE

while i >= 1:
    i = i - 1
    print(s)
    s = s + TREE