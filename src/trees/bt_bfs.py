from collections import deque


def bfs(tree, value):
    queue = deque()
    queue.append(tree)
    while len(queue) > 0:
        current = queue.popleft()
        if current.value == value:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False
