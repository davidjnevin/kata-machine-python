import pytest

from src.data_structures.singly_linked_list import Singly_linked_list


def test_prepend():
    sll = Singly_linked_list()
    sll.prepend(1)
    assert sll.head.data == 1
    sll.prepend(2)
    assert sll.head.data == 2
    sll.prepend(3)
    assert sll.head.data == 3


def test_get_at_emply_linked_list():
    sll = Singly_linked_list()

    with pytest.raises(ValueError):
        sll.get_at(3)


def test_get_at_IndexError():
    sll = Singly_linked_list()
    sll.prepend(1)
    sll.prepend(2)
    sll.prepend(3)

    with pytest.raises(IndexError):
        sll.get_at(22)


def test_get_at_valid_index():
    sll = Singly_linked_list()
    sll.prepend(1)
    sll.prepend(2)
    sll.prepend(3)
    # [3, 2, 1 ]
    assert sll.get_at(0) == 3
    assert sll.get_at(1) == 2
    assert sll.get_at(2) == 1


def test_append():
    sll = Singly_linked_list()

    sll.append(1)
    assert sll.get_at(0) == 1

    sll.append(2)
    assert sll.get_at(1) == 2

    sll.append(3)
    assert sll.get_at(2) == 3


def test_insertAt_invalid_index():
    sll = Singly_linked_list()
    with pytest.raises(IndexError):
        sll.insertAt(3, 4)
    with pytest.raises(IndexError):
        sll.insertAt(-1, 4)
    assert sll.length == 0


def test_insertAt():
    sll = Singly_linked_list()
    sll.append(0)
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    sll.append(7)
    assert sll.length == 8
    # [0, 1, 2, 3, 4, 5, 6, 7]
    sll.insertAt(4, 23)
    # [0, 1, 2, 3, 23, 4, 5, 6, 7]
    assert sll.get_at(3) == 3
    assert sll.get_at(4) == 23
    assert sll.get_at(5) == 4
    assert sll.length == 9


def test_insertAt_in_empty_list_with_idx_as_zero():
    sll = Singly_linked_list()
    sll.insertAt(0, 23)
    assert sll.length == 1
    assert sll.get_at(0) == 23


def test_removeAt_empty_list():
    sll = Singly_linked_list()
    with pytest.raises(IndexError):
        sll.removeAt(0)
    assert sll.length == 0


def test_removeAt_from_one_element_list():
    sll = Singly_linked_list()
    sll.append(4)
    sll.removeAt(0)
    assert sll.length == 0


def test_removeAt_tail():
    sll = Singly_linked_list()
    sll.append(0)
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    assert sll.length == 7
    # [0, 1, 2, 3, 4, 5, 6]
    sll.removeAt(6)
    # [0, 1, 2, 3, 4, 5]
    assert sll.get_at(5) == 5
    with pytest.raises(IndexError):
        sll.get_at(6)
    assert sll.length == 6


def test_removeAt():
    sll = Singly_linked_list()
    sll.append(0)
    sll.append(1)
    sll.append(2)
    sll.append(23)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    sll.append(6)
    assert sll.length == 8
    print(sll)
    # [0, 1, 2, 23, 3, 4, 5, 6, 7]
    sll.removeAt(3)
    # [0, 1, 2, 3, 4, 5, 6, 7]

    print(sll)
    assert sll.get_at(2) == 2
    assert sll.get_at(3) == 3
    assert sll.get_at(4) == 4
    assert sll.length == 7
