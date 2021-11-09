"""Practice with dictionaries."""

__author__ = "730396074"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Replaces keys with their values and values with their keys."""
    dictionary_keys: list[str] = []
    dictionary_values: list[str] = []
    new_dictionary: dict[str, str] = {}
    i: int = 0

    for key in dictionary:
        dictionary_keys.append(key)

    for value in dictionary:
        dictionary_values.append(dictionary[value])

    while i < len(dictionary_keys):
        new_dictionary[dictionary_values[i]] = dictionary_keys[i]
        i += 1

    new_dictionary_keys: list[str] = list(new_dictionary.values())

    if len(new_dictionary_keys) != len(dictionary_keys):
        raise KeyError("Had repeated values in the dictionary.")

    return new_dictionary


def favorite_color(dict_colors: dict[str, str]) -> str:
    """Finds the most recurring favorite color in a dictionary."""
    color_list: list[str] = []
    occuring_list: list[int] = []
    popping_list: list[int] = []

    for value in dict_colors:
        color_list.append(dict_colors[value])

    i: int = 0
    while i < len(color_list):
        c: int = 1
        h: int = 0
        while h < len(color_list):
            if h != i:
                if color_list[h] == color_list[i]:
                    c += 1
            h += 1
        occuring_list.append(c)
        popping_list.append(c)
        i += 1

    t: int = 0
    t2: int = 1
    while len(popping_list) > 1:
        if popping_list[t] > popping_list[t2]:
            popping_list.pop(1)
        else:
            popping_list.pop(0)

    most_occuring_number: int = popping_list[0]
    i: int = 0
    while i < len(occuring_list):
        if most_occuring_number == occuring_list[i]:
            return color_list[i]
        i += 1
    return color_list[i]


def count(count_list: list[str]) -> dict[str, int]:
    """Counts how many times a word appears in a list and creates a dictionary."""
    new_dictionary: dict[str, int] = {}
    i: int = 0
    while i < len(count_list):
        c: int = 1
        h: int = 0
        while h < len(count_list):
            if h != i:
                if count_list[h] == count_list[i]:
                    c += 1
            h += 1
        new_dictionary[count_list[i]] = c
        i += 1
    return new_dictionary
