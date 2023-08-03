from src.trees.bt_compare import compare_binary_trees as compare

# Binary Tree Comaprison Test


def test_compare_binary_trees(
    binary_tree, another_binary_tree, yet_another_binary_tree
):
    assert compare(binary_tree, another_binary_tree) is False
    assert compare(binary_tree, yet_another_binary_tree) is True
