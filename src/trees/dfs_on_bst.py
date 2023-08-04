def search(curr, neddle) -> bool:
    if not curr:
        return False
    if curr.value == neddle:
        return True
    if curr.value < neddle:
        return search(curr.right, neddle)
    return search(curr.left, neddle)


def dfs(head, needle) -> bool:
    return search(head, needle)
