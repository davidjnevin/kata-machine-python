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
