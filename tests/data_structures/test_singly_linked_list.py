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


# def test_append():
#     sll = Singly_linked_list()
#     sll.append(1)
#     assert sll.head.data == 1
#     sll.append(2)
#     assert sll.get_at(1) == 2
#     sll.append(3)
#     assert sll.get_at(2) == 3
