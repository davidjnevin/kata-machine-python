def sum_recursion(n):
    # base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + sum_recursion(n - 1)
