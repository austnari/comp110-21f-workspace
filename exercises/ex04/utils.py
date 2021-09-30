"""List utility functions."""

__author__ = "730396074"


def all(xs: list[int], x: int) -> bool:
    """Tests to see if an int equals everything in a list."""
    i: int = 0
    c: int = 0
    while i < len(xs):
        if xs[i] == x:
            c += 1
        i += 1
    if len(xs) == 0:
        return False
    if c == len(xs):
        return True
    return False


def is_equal(xs: list[int], ys: list[int]) -> bool:
    """Tests to see if two different lists are exactly equal to one another."""
    i: int = 0
    c: int = 0
    if len(xs) == len(ys):
        while i < len(xs):
            if xs[i] == ys[i]:
                c += 1
            i += 1
        if c == len(xs) and len(ys):
            return True
        if len(xs) == 0:
            return True
        else:
            return False
    else:
        return False


def max(input: list[int]) -> int:
    """Function to find the largest value in a list."""
    t: int = 0
    t2: int = 1
    while len(input) > 1:
        if input[t] > input[t2]:
            input.pop(1)
        else:
            input.pop(0)
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    return input[0]