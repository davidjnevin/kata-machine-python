from src.trees.bt_pre_order_search import pre_order


def test_in_order_binary_tree_traversal(binary_tree):
    assert pre_order(binary_tree) == [
        20,
        10,
        5,
        7,
        15,
        50,
        30,
        29,
        45,
        100,
    ]
