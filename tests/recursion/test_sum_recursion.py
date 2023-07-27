from src.recursion.sum_recursion import sum_recursion


def test_sum_recursion():
    assert sum_recursion(5) == 15

    assert sum_recursion(10) == 55

    assert sum_recursion(0) == 0
