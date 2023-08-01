from src.sort.quick_sort import quick_sort


def test_quick_sort():
    arr = [9, 3, 7, 4, 69, 420, 42, 100, 33, 1, 90]

    quick_sort(arr)
    assert arr == [1, 3, 4, 7, 9, 33, 42, 69, 90, 100, 420]
