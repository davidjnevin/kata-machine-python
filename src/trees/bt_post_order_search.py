from src.trees.binary_node import BinaryNode


def walk(curr: BinaryNode | None, path: list[int]) -> None:
    if curr is None:
        return

    # post-order: left, right, root
    # pre
    # recurse
    walk(curr.left, path)
    walk(curr.right, path)
    path.append(curr.value)
    # post


def post_order(head: BinaryNode) -> list[int]:
    path: list = []
    walk(head, path)
    return path
