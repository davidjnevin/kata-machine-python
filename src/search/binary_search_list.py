import math

# Binary Search Algorithm
# Time Complexity: O(log n)


def binary_search(myList: list, item: int):
    if myList == []:
        raise ValueError()

    lo: int = 0
    hi: int = len(myList)

    keepgoing = lo <= hi
    found = False

    while keepgoing:
        # set a midpoint to guess
        # midpoint should take into consideration
        # adjustment for to find mid of upper half too
        mid: int = math.floor(lo + (hi - lo) / 2)
        guess: int = myList[mid]
        if item == guess:
            return True
        if item > guess:
            lo = mid + 1
        if item < guess:
            hi = mid
        if lo >= hi:
            keepgoing = False
    return found
