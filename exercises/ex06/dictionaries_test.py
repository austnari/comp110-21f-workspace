"""Unit tests for dictionary functions."""


from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730396074"


def test_invert_simple_dict() -> None:
    """Tests to see if invert can invert a list with two keys."""
    dictionary: dict[str, str] = {'a': 'b', 'b': 'c'}
    assert invert(dictionary) == {'b': 'a', 'c': 'b'}


def test_invert_long_dict() -> None:
    """Tests to see if invert can invert a long dict."""
    dictionary: dict[str, str] = {'red': 'apple', 'blue': 'bird', 'yellow': 'flower', 'green': 'tree', 'purple': 'rain', 'orange': 'cone'}
    assert invert(dictionary) == {'apple': 'red', 'bird': 'blue', 'flower': 'yellow', 'tree': 'green', 'rain': 'purple', 'cone': 'orange'}


def test_invert_dict_same() -> None:
    """Tests to see if invert can still invert when a dict has the same key and value."""
    dictionary: dict[str, str] = {'Austin': 'Austin', 'Nario': 'Nario'}
    assert invert(dictionary) == {'Austin': 'Austin', 'Nario': 'Nario'}


def test_favorite_color_long_dict() -> None:
    """Tests to see if function can find the most recurring color in a long dict."""
    dictionary: dict[str, str] = {"Austin": "blue", "Sean": "red", "Gary": "orange", "Bernadette": "blue", "Ben": "yellow", "Joe": "yellow", "Candice": "blue", "Walt": "yellow", "Walter Jr": "yellow"}
    assert favorite_color(dictionary) == "yellow"


def test_favorite_color_one_key() -> None:
    """Tests to see if function works with a one key-value dict."""
    dictionary: dict[str, str] = {"Austin": "blue"}
    assert favorite_color(dictionary) == "blue"


def test_favorite_color_no_favorite_color() -> None:
    """Tests to see if funtion returns first color if there is no color that occurs more than once."""
    dictionary: dict[str, str] = {"Sean": "red", "Austin": "blue", "Gary": "orange", "Bernadette": "purple"}
    assert favorite_color(dictionary) == "red"


def test_count_all_the_same() -> None:
    """Tests to see if function creates dictionary with a list of all of the same words."""
    input_list: list[str] = ["hi", "hi", "hi", "hi"]
    assert count(input_list) == {'hi': 4}


def test_count_long_list() -> None:
    """Tests to see if function works with a long list."""
    input_list: list[str] = ["hello", "hello", "hi", "good morning", "hi", "hello", "good morning", "hola", "hola", "greetings", "hi", "greetings", "good morning", "hola"]
    assert count(input_list) == {'hello': 3, 'hi': 3, 'good morning': 3, 'hola': 3, 'greetings': 2}


def test_count_one_value_list() -> None:
    """Tests to see if function works with a list that is only one value."""
    input_list: list[str] = ["lonely"]
    assert count(input_list) == {'lonely': 1}