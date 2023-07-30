from pprint import pprint

# Solve a square maze


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


def draw_path(data: list[str], path: list[Point]) -> list[str]:
    data2 = [list(row) for row in data]
    for p in path:
        if data2[p.y] and data2[p.y][p.x]:
            data2[p.y][p.x] = "*"
    return ["".join(d) for d in data2]


# differencial directions
directions = [
    [0, -1],  # up
    [1, 0],  # right
    [0, 1],  # down
    [-1, 0],  # left
]


def walk_maze(
    maze: list[str],
    wall: str,
    curr: Point,
    end: Point,
    seen: list[list[bool]],
    path: list[Point],
) -> bool:
    # base case
    # for this solution maze is square
    # Off the map,
    if curr.x < 0 or curr.x >= len(maze[0]) or curr.y < 0 or curr.y >= len(maze):
        return False
    # On a wall
    if maze[curr.y][curr.x] == wall:
        return False
    # It's the end
    if curr.y == end.y and curr.y == end.y:
        # since finding the end here would end the recursion
        # our final end tile would not be pushed in at post recursion
        path.append(end)
        return True
    # If we have seen this before
    if seen[curr.y][curr.x]:
        return False

    # recursion
    # pre recursion
    seen[curr.y][curr.x] = True
    path.append(curr)  # pushes 'curr' onto the stack

    # recursion
    for i in range(len(directions)):
        [x, y] = directions[i]
        if walk_maze(maze, wall, Point(curr.x + x, curr.y + y), end, seen, path):
            return True

    # post recursion
    path.pop()  # pops the last visit point off the stack

    return False


def maze_solver(maze: list[str], wall: str, start: Point, end: Point) -> list[Point]:
    #
    path: list[Point] = []
    seen: list[list[bool]] = [
        [False for _ in range(len(maze[0]))] for _ in range(len(maze))
    ]

    walk_maze(maze, wall, start, end, seen, path)
    pprint(maze)
    pprint(draw_path(maze, path))
    return path
