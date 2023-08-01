from src.trees.binary_node import BinaryNode


def walk(curr: BinaryNode | None, path: list[int]) -> None:
    if curr is None:
        return

    # in-order: left, right, visit
    # pre
    # recurse
    walk(curr.left, path)
    path.append(curr.value)
    walk(curr.right, path)
    # post


def in_order(head: BinaryNode) -> list[int]:
    path: list = []
    walk(head, path)
    return path
