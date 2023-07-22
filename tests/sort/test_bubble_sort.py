from src.sort.bubble_sort import bubble_sort


def test_bubble_sort():
    arr = [9, 3, 7, 4, 69, 420, 42]

    bubble_sort(arr)
    expected_result = [3, 4, 7, 9, 42, 69, 420]

    assert arr == expected_result, f"Expected {expected_result}, but got {arr}"
