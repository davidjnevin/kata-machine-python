from src.trees.df_insert_on_bst import df_insert
from src.trees.dfs_on_bst import dfs


def test_bt_dfs(binary_tree):
    assert dfs(binary_tree, 111) is False
    df_insert(binary_tree, 111)
    assert dfs(binary_tree, 111) is True
