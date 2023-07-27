from src.recursion.factorial_recursion import factorial_recursion


def test_sum_recursion():
    assert factorial_recursion(5) == 5 * 4 * 3 * 2 * 1

    assert factorial_recursion(10) == 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

    assert factorial_recursion(0) == 0
