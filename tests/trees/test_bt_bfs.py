from src.trees.bt_bfs import bfs


def test_bt_bfs(binary_tree):
    assert bfs(binary_tree, 45) is True
    assert bfs(binary_tree, 7) is True
    assert bfs(binary_tree, 69) is False
