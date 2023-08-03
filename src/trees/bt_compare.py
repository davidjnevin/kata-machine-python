def compare_binary_trees(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False

    # recursively compare left and right subtrees and values
    # if all are equal, return True

    return (
        a.value == b.value
        and compare_binary_trees(a.left, b.left)
        and compare_binary_trees(a.right, b.right)
    )
