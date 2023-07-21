import pytest

from src.search.binary_search_list import binary_search


def test_binary_search_list_empty_list():
    myList = []

    with pytest.raises(ValueError):
        assert binary_search(myList, 3)


def test_binary_search_list():
    myList = [0, 3, 7, 8, 9, 15, 33, 41, 63, 89, 2001]

    assert binary_search(myList, 3)  # index 1
    assert binary_search(myList, 15)  # first mid point
    assert binary_search(myList, 2001)  # last index
    assert binary_search(myList, 0)  # index 0

    assert binary_search(myList, 11) is False  # not in list below mid
    assert binary_search(myList, 34) is False  # not in list above mid


def test_binary_search_list_with_one_element():
    myList = [9418]

    assert binary_search(myList, 9418)
    assert binary_search(myList, 10) is False
