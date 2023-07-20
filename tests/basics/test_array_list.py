from typing import cast

import pytest
from _pytest.python_api import raises

import src.basics.array_list as array_list


def test_append():
    a = array_list.ArrayList(capacity=10)
    a.append(1)
    assert a.length == 1
    a.append(2)
    assert a.length == 2


def test_resize():
    a = array_list.ArrayList(capacity=10)
    for i in range(10):
        a.append(i)

    assert a.length == 10
    assert a.capacity == 10

    a.append(11)
    assert a.length == 11
    assert a.capacity == 20


def test_get():
    a = array_list.ArrayList(capacity=10)
    for i in range(10):
        a.append(i)

    assert a.get(0) == 0
    assert a.get(9) == 9


def test_get_invalid_index_wher_index_is_greater_than_length():
    a = array_list.ArrayList(capacity=10)

    for i in range(5):
        a.append(i)
    with pytest.raises(IndexError):
        assert a.get(5)


def test_get_invalid_index_wher_index_is_negative():
    a = array_list.ArrayList(capacity=10)

    for i in range(5):
        a.append(i)
    with pytest.raises(IndexError):
        assert a.get(-1)


def test_prepend():
    a = array_list.ArrayList(capacity=10)

    for i in range(5):
        a.append(i)

    array_length = a.length

    a.prepend(11)
    assert a.get(0) == 11

    # check all values exist at the correct index
    assert a.data == [11, 0, 1, 2, 3, 4, None, None, None, None]

    assert a.length == array_length + 1


def test_prepend_to_full_array():
    a = array_list.ArrayList(capacity=10)

    # Fill the first ten available slots
    for i in range(10):
        a.append(i)

    array_length = a.length
    assert array_length == 10
    a.prepend(10)
    assert a.get(0) == 10

    # check all values exist at the correct index
    assert a.data == [10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, None, None, None]

    assert a.length == array_length + 1

    assert a.capacity == 20


def test_remove_at_index_reduces_length():
    a = array_list.ArrayList(capacity=10)
    for i in range(5):
        a.append(i)

    a.remove_at(0)
    assert a.length == 4


def test_remove_at_index_removes_item_at_index():
    a = array_list.ArrayList(capacity=10)
    for i in range(5):
        a.append(i)

    a.remove_at(0)
    for i in range(a.length):
        assert a.get(i) == i + 1


def test_remove_at_invalid_index_returns_IndexError():
    a = array_list.ArrayList(capacity=10)
    for i in range(5):
        a.append(i)

    with pytest.raises(IndexError):
        a.remove_at(5)


def test_remove_item_that_exists_in_arraryList():
    a = array_list.ArrayList(capacity=10)
    for i in range(5):
        a.append(i)

    a.remove(3)
    assert a.length == 4
    assert str(a) == '[0, 1, 2, 4, None, None, None, None, None, None]'


def test_remove_item_that_does_not_exist_in_arraryList():
    a = array_list.ArrayList(capacity=10)
    for i in range(5):
        a.append(i)
    original_length = a.length

    with pytest.raises(ValueError, match="77 not found"):
        a.remove(77)
    assert a.length == original_length
    assert str(a) == '[0, 1, 2, 3, 4, None, None, None, None, None]'
