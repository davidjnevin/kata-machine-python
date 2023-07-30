from src.recursion.maze_solver import Point, maze_solver


def test_maze_solver():
    maze = [
        "XXXXXXXXXX X",
        "X        X X",
        "X        X X",
        "X XXXXXXXX X",
        "X          X",
        "X XXXXXXXXXX",
    ]

    maze_result: list[Point] = [
        Point(10, 0),
        Point(10, 1),
        Point(10, 2),
        Point(10, 3),
        Point(10, 4),
        Point(9, 4),
        Point(8, 4),
        Point(7, 4),
        Point(6, 4),
        Point(5, 4),
        Point(4, 4),
        Point(3, 4),
        Point(2, 4),
        Point(1, 4),
        Point(1, 5),
    ]
    result = maze_solver(maze=maze, wall="X", start=Point(10, 0), end=Point(1, 5))
    # // there is only one path through
    # expect(drawPath(maze, result)).toEqual(drawPath(maze, mazeResult));
    assert draw_path(maze, result) == draw_path(maze, maze_result)


def draw_path(data: list[str], path: list[Point]) -> list[str]:
    data2 = [list(row) for row in data]
    for p in path:
        if data2[p.y] and data2[p.y][p.x]:
            data2[p.y][p.x] = "*"
    return ["".join(d) for d in data2]
