

def head(data_cols: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Shortens a dictionary so only 'n' values are given for each key."""
    dictionary_keys: list[str] = []

    for key in dictionary:
        dictionary_keys.append(key)

    result: dict[str, list[str]] = {}
    d: int = 0
    while d != len(data_cols):
        new_values: list[str] = []
        c: int = 0

        while len(new_values) != n:
            new_values.append(data_cols[dictionary_keys[d]][c])
            c += 1

        result[keys[d]] = new_values
        d += 1

    return result


dictionary: dict[str, list[str]] = {"1": ["a", "b", "c", "d", "e", "f"], "2": ["g", "h", "i", "j", "k", "l"], "3": ["m", "n", "o", "p", "q", "r"]}
keys: list[str] = ["1", "2", "3"]
want: list[str] = ["2", "3"]


def select(data: dict[str, list[str]], wanted_columns: list[str]) -> dict[str, list[str]]:
    """Selects certain columns to be the only one's displayed."""
    dictionary_keys: list[str] = []

    for key in data:
        dictionary_keys.append(key)
    
    result: dict[str, list[str]] = {}
    i: int = 0
    while i < len(wanted_columns):
        d: int = 0
        while d != len(data):
            if dictionary_keys[d] == wanted_columns[i]:
                result[dictionary_keys[d]] = list(data[dictionary_keys[d]])
            d += 1
        i += 1

    return result


dictionary: dict[str, list[str]] = {"1": ["a", "b", "c", "d", "e", "f"], "2": ["g", "h", "i", "j", "k", "l"], "3": ["m", "n", "o", "p", "q", "r"]}
dictionary2: dict[str, list[str]] = {"1": ["aa", "bb", "cc", "dd", "ee", "ff"], "2": ["gg", "hh", "ii", "jj", "kk", "ll"], "3": ["mm", "nn", "oo", "pp", "qq", "rr"]}


def concat(data: dict[str, list[str]], data2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column-based tables."""
    result: dict[str, list[str]] = {}
    for cols in data:
        value: list[str] = data[cols]
        result[cols] = value
    for cols in data2:
        if cols in result:
            value: list[str] = data2[cols]
            result[cols] += value
        else:
            value: list[str] = data2[cols]
            result[cols] = value
    return result



print(concat(dictionary, dictionary2))