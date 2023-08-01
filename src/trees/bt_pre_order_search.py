from src.trees.binary_node import BinaryNode


def walk(curr: BinaryNode | None, path: list[int]) -> None:
    if curr is None:
        return

    # Pre-order: root, left, right
    # pre
    path.append(curr.value)
    # recurse
    walk(curr.left, path)
    walk(curr.right, path)
    # post


def pre_order(head: BinaryNode) -> list[int]:
    path: list = []
    walk(head, path)
    return path
