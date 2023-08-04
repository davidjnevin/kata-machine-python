from src.trees.df_delete_on_bst import df_delete
from src.trees.dfs_on_bst import dfs


def test_bt_df_delete_on_leaf(binary_search_tree):
    assert dfs(binary_search_tree, 7) is True
    df_delete(binary_search_tree, 7)
    assert dfs(binary_search_tree, 7) is False


def test_bt_df_delete_on_node_with_one_child(binary_search_tree):
    assert dfs(binary_search_tree, 17) is True
    df_delete(binary_search_tree, 17)
    assert dfs(binary_search_tree, 17) is False


def test_bt_df_delete_on_node_with_two_children(binary_search_tree):
    assert dfs(binary_search_tree, 25) is True
    df_delete(binary_search_tree, 25)
    assert dfs(binary_search_tree, 25) is False
