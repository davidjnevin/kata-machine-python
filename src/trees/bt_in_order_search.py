from src.trees.binary_node import BinaryNode


def walk(curr: BinaryNode | None, path: list[int]) -> None:
    if curr is None:
        return

    # in-order: left, visit, right
    # pre
    walk(curr.left, path)
    # recurse
    path.append(curr.value)
    # post
    walk(curr.right, path)


def in_order(head: BinaryNode) -> list[int]:
    path: list = []
    walk(head, path)
    return path
