from src.trees.binary_node import BinaryNode


def insert(curr, value):
    if curr.value < value:
        if curr.right:
            insert(curr.right, value)
        else:
            curr.right = BinaryNode(value)
    else:
        if curr.left:
            insert(curr.left, value)
        else:
            curr.left = BinaryNode(value)


def df_insert(tree, value):
    insert(tree, value)
