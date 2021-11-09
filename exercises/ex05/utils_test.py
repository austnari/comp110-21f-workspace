"""Unit tests for list utility functions."""

__author__ = "730396074"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_all_odds() -> None:
    """Tests to see if function returns an empty list if given all odd values in a list."""
    xs: list[int] = [1, 3, 5]
    assert only_evens(xs) == []


def test_only_evens_all_evens_negative_values() -> None:
    """Tests if the function works with a given list comprised of negative int values."""
    xs: list[int] = [-1, -2, -3, -4, -5, -6]
    assert only_evens(xs) == [-2, -4, -6]


def test_only_evens_many_items() -> None:
    """Tests the function with a list with a variety of int values."""
    xs: list[int] = [1, 3, 4, 2, 100, 65, 72, 89, 8]
    assert only_evens(xs) == [4, 2, 100, 72, 8]


def test_sub_empty_list() -> None:
    """Tests to see if the function returns an empty list if given an empty list."""
    xs: list[int] = []
    x: int = 0
    y: int = 0
    assert sub(xs, x, y) == []


def test_sub_negative_and_large_indices() -> None:
    """Tests to see if a negative first index value and a too large second index value, still produce a list."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    x: int = -1
    y: int = 7
    assert sub(xs, x, y) == [1, 2, 3, 4, 5, 6]


def test_sub_many_items() -> None:
    """Tests the function's ability to function with a variety of int values."""
    xs: list[int] = [1, 456, 5, 22, 39, 90, -42, 43, -9, 91, 203, 69, 7337]
    x: int = 4
    y: int = 10
    assert sub(xs, x, y) == [39, 90, -42, 43, -9, 91]


def test_concat_two_empty_lists() -> None:
    """Tests to see if it returns an empty list if both lists are empty."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_two_lists_with_many_items() -> None:
    """Tests to see if the function will concatenate two functions with many items each."""
    xs: list[int] = [3, 56, 82, 90, 194, 439, 2]
    ys: list[int] = [4, 78, 23, 2, 999, 10, 78, 34, 21, 785, 405]
    assert concat(xs, ys) == [3, 56, 82, 90, 194, 439, 2, 4, 78, 23, 2, 999, 10, 78, 34, 21, 785, 405]


def test_concat_one_list_empty() -> None:
    """Tests to see if the function will return the other list if one list is empty."""
    xs: list[int] = []
    ys: list[int] = [1]
    assert concat(xs, ys) == [1]