"""List utility functions part 2."""

__author__ = "730396074"


def only_evens(xs: list[int]) -> list[int]:
    """Removes all odd numbers in a list of integers."""
    i: int = 0
    c: int = 0
    if len(xs) == 0:
        return(xs)
    while i <= len(xs):
        if xs[c] % 2 != 0:
            xs.pop(c)
        else:
            c += 1
            i += 1
        if i == len(xs):
            return xs
    return xs


def sub(xs: list[int], x: int, y: int) -> list[int]:
    """Returns a subset of a list when given a list and two indices."""
    new_list: list[int] = []
    if x < 0:
        x = 0
    if y > len(xs):
        y = len(xs)
    if len(xs) == 0:
        return new_list
    while x < y:
        new_list.append(int(xs[x]))
        x += 1
    return new_list


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Concatenates two lists together."""
    new_list: list[int] = []
    if len(xs) + len(ys) == 0:
        return []
    if len(xs) == 0:
        return ys
    if len(ys) == 0:
        return xs
    i: int = 0
    while i < len(xs):
        new_list.append(int(xs[i]))
        i += 1
    c: int = 0
    while c < len(ys):
        new_list.append(int(ys[c]))
        c += 1
    return new_list