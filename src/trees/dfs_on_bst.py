def search(curr, needle) -> bool:
    if not curr:
        return False
    # if not curr.value:
    #     return False
    if curr.value == needle:
        return True
    if curr.value < needle:
        return search(curr.right, needle)
    return search(curr.left, needle)


def dfs(head, needle) -> bool:
    return search(head, needle)
