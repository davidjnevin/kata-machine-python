import pytest

from src.data_structures.doubly_linked_list import Doubly_linked_list


def test_prepend():
    dll = Doubly_linked_list()
    dll.prepend(1)
    assert dll.head.data == 1
    dll.prepend(2)
    assert dll.head.data == 2
    dll.prepend(3)
    assert dll.head.data == 3


def test_get_at_emply_linked_list():
    dll = Doubly_linked_list()

    with pytest.raises(IndexError):
        dll.get_at(3)


def test_get_at_IndexError():
    dll = Doubly_linked_list()
    dll.prepend(1)
    dll.prepend(2)
    dll.prepend(3)

    with pytest.raises(IndexError):
        dll.get_at(22)


def test_get_at_valid_index():
    dll = Doubly_linked_list()
    dll.prepend(1)
    assert dll.head.data == 1
    dll.prepend(2)
    assert dll.head.data == 2
    dll.prepend(3)
    assert dll.head.data == 3
    # [3, 2, 1 ]
    assert dll.get_at(0) == 3
    assert dll.get_at(1) == 2
    assert dll.get_at(2) == 1


def test_append():
    dll = Doubly_linked_list()

    dll.append(1)
    assert dll.get_at(0) == 1
    assert dll.head.data == 1

    dll.append(2)
    assert dll.get_at(1) == 2
    assert dll.head.data == 1

    dll.append(3)
    assert dll.get_at(2) == 3
    assert dll.head.data == 1


def test_insertAt_invalid_index():
    dll = Doubly_linked_list()
    with pytest.raises(IndexError):
        dll.insertAt(3, 4)
    with pytest.raises(IndexError):
        dll.insertAt(-1, 4)
    assert dll.length == 0


def test_insertAt():
    dll = Doubly_linked_list()
    dll.append(0)
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    dll.append(7)
    assert dll.length == 8
    # [0, 1, 2, 3, 4, 5, 6, 7]
    dll.insertAt(4, 23)
    # [0, 1, 2, 3, 23, 4, 5, 6, 7]
    assert dll.get_at(3) == 3
    assert dll.get_at(4) == 23
    assert dll.get_at(5) == 4
    assert dll.length == 9


def test_insertAt_in_empty_list_with_idx_as_zero():
    dll = Doubly_linked_list()
    dll.insertAt(0, 23)
    assert dll.length == 1
    assert dll.get_at(0) == 23
    assert dll.head.data == 23


def test_removeAt_empty_list():
    dll = Doubly_linked_list()
    with pytest.raises(IndexError):
        dll.removeAt(0)
    assert dll.length == 0


def test_removeAt_from_one_element_list():
    dll = Doubly_linked_list()
    dll.append(4)
    dll.removeAt(0)
    assert dll.length == 0


def test_removeAt_head_from_multi_element_list():
    dll = Doubly_linked_list()
    dll.append(4)
    dll.append(5)
    dll.removeAt(0)
    assert dll.length == 1
    assert dll.head.data == 5


def test_removeAt_tail():
    dll = Doubly_linked_list()
    dll.append(0)
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    assert dll.length == 7
    # [0, 1, 2, 3, 4, 5, 6]
    dll.removeAt(6)
    # [0, 1, 2, 3, 4, 5]
    assert dll.get_at(5) == 5
    with pytest.raises(IndexError):
        dll.get_at(6)
    assert dll.length == 6


def test_removeAt():
    dll = Doubly_linked_list()
    dll.append(0)
    dll.append(1)
    dll.append(2)
    dll.append(23)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    assert dll.length == 8
    print(dll)
    # [0, 1, 2, 23, 3, 4, 5, 6, 7]
    dll.removeAt(3)
    # [0, 1, 2, 3, 4, 5, 6, 7]

    print(dll)
    assert dll.get_at(2) == 2
    assert dll.get_at(3) == 3
    assert dll.get_at(4) == 4
    assert dll.length == 7


def test_remove():
    dll = Doubly_linked_list()
    dll.append(0)
    dll.append(1)
    dll.append(2)
    dll.append(23)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    assert dll.length == 8
    # [0, 1, 2, 23, 3, 4, 5, 6, 7]
    dll.remove(23)
    # [0, 1, 2, 3, 4, 5, 6, 7]
    assert dll.get_at(2) == 2
    assert dll.get_at(3) == 3
    assert dll.get_at(4) == 4
    assert dll.length == 7


def test_remove_non_existant_value():
    dll = Doubly_linked_list()
    dll.append(0)
    dll.append(1)
    dll.append(2)
    dll.append(23)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    assert dll.length == 8
    # [0, 1, 2, 23, 3, 4, 5, 6, 7]
    with pytest.raises(ValueError):
        dll.remove(24)
    # [0, 1, 2, 3, 4, 5, 6, 7]
    assert dll.length == 8
