import pytest

from src.trees.binary_node import BinaryNode


# Define a tree
@pytest.fixture
def binary_tree():
    return BinaryNode(
        20,
        left=BinaryNode(
            10,
            left=BinaryNode(
                5,
                right=BinaryNode(7),
                left=None,
            ),
            right=BinaryNode(15),
        ),
        right=BinaryNode(
            50,
            left=BinaryNode(
                30,
                left=BinaryNode(29),
                right=BinaryNode(45),
            ),
            right=BinaryNode(100),
        ),
    )


# Define another tree
@pytest.fixture
def another_binary_tree():
    return BinaryNode(
        20,
        left=BinaryNode(
            10,
            left=BinaryNode(
                5,
                right=BinaryNode(7),
                left=BinaryNode(
                    30,
                    left=BinaryNode(29),
                    right=BinaryNode(45),
                ),
            ),
            right=BinaryNode(15),
        ),
        right=BinaryNode(
            50,
            left=None,
            right=BinaryNode(100),
        ),
    )


# Define yet another tree
@pytest.fixture
def yet_another_binary_tree():
    return BinaryNode(
        20,
        left=BinaryNode(
            10,
            left=BinaryNode(
                5,
                right=BinaryNode(7),
                left=None,
            ),
            right=BinaryNode(15),
        ),
        right=BinaryNode(
            50,
            left=BinaryNode(
                30,
                left=BinaryNode(29),
                right=BinaryNode(45),
            ),
            right=BinaryNode(100),
        ),
    )


@pytest.fixture
def binary_search_tree():
    return BinaryNode(
        12,
        left=BinaryNode(
            8,
            left=BinaryNode(7),
            right=BinaryNode(9),
        ),
        right=BinaryNode(
            25,
            left=BinaryNode(
                17,
                left=None,
                right=BinaryNode(19),
            ),
            right=BinaryNode(30),
        ),
    )
