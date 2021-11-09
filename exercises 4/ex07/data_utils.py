"""Utility functions."""

__author__ = "730396074"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(data_cols: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Shortens a dictionary so only 'n' values are given for each key."""
    dictionary_keys: list[str] = []

    for key in data_cols:
        dictionary_keys.append(key)

    result: dict[str, list[str]] = {}
    d: int = 0
    while d != len(data_cols):
        new_values: list[str] = []
        c: int = 0

        while len(new_values) != n:
            new_values.append(data_cols[dictionary_keys[d]][c])
            c += 1

        result[dictionary_keys[d]] = new_values
        d += 1

    return result


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


def concat(data: dict[str, list[str]], data2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column-based tables."""
    
    result: dict[str, list[str]] = {}
    for key in data:
        value: list[str] = data[key]
        result[key] = value

    for key in data2:
        if key in result:
            value: list[str] = data2[key]
            result[key] += value
        else:
            value: list[str] = data2[key]
            result[key] = value

    return result


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