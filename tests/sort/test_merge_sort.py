from src.sort.merge_sort import merge_sort


def test_merge_sort():
    arr = [9, 3, 7, 4, 69, 420, 42]

    merge_sort(arr)
    assert arr == [3, 4, 7, 9, 42, 69, 420]
