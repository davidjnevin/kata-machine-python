# Not in the original Primagen Course, but added for fun.


def factorial_recursion(n):
    # base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n * factorial_recursion(n - 1)
