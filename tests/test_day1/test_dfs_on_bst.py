from src.trees.dfs_on_bst import dfs


def test_bt_dfs(binary_tree):
    assert dfs(binary_tree, 45) is True
    assert dfs(binary_tree, 7) is True
    assert dfs(binary_tree, 69) is False
