import random

from src.search.two_crystal_balls import search_break_point


def test_two_crystal_balls_break():
    data_capacity = 10
    idx = random.randint(0, data_capacity)
    data = []
    for _ in range(data_capacity):
        data.append(False)
    for i in range(idx, data_capacity):
        data[i] = True

    # breakpoint()
    assert search_break_point(data) == idx


def test_two_crystal_balls_break_with_no_solution():
    no_solution_array = []
    for _ in range(900):
        no_solution_array.append(False)

    assert search_break_point(no_solution_array) == -1
