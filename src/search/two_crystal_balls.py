import math
from math import sqrt


def search_break_point(data):
    leap: int = math.floor(sqrt(len(data)))
    lo = 0
    hi = leap

    keepgoing = True

    while keepgoing:
        if hi <= len(data) - 1:
            if data[hi]:
                for i in range(lo, hi + 1):
                    if data[i]:
                        return i
        elif hi >= len(data):
            hi = len(data) - 1
            if data[hi]:
                for i in range(lo, hi):
                    if data[i]:
                        return i
                    else:
                        break
        hi += leap
        lo += leap
        keepgoing = lo < len(data) - 1

    return -1
