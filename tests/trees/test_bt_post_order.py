from src.trees.bt_post_order_search import post_order


def test_in_order_binary_tree_traversal(binary_tree):
    assert post_order(binary_tree) == [
        7,
        5,
        15,
        10,
        29,
        45,
        30,
        100,
        50,
        20,
    ]
