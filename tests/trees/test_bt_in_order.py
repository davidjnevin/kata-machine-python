from src.trees.bt_in_order_search import in_order


def test_in_order_binary_tree_traversal(binary_tree):
    assert in_order(binary_tree) == [
        5,
        7,
        10,
        15,
        20,
        29,
        30,
        45,
        50,
        100,
    ]
