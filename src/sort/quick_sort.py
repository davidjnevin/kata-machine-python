# Quick Sort O(n log(n)) -> O(n2)


def qs(arr: list[int], lo: int, hi: int) -> None:
    if lo >= hi:
        return

    pivot_idx = partition(arr, lo, hi)
    qs(arr, lo, pivot_idx - 1)
    qs(arr, pivot_idx + 1, hi)


def partition(arr: list[int], lo: int, hi: int) -> int:
    pivot: int = arr[hi]
    idx: int = lo - 1

    # weak sort
    for i in range(lo, hi):
        if arr[i] <= pivot:
            idx += 1
            # swap
            tmp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = tmp
    # swap the pivot
    idx += 1
    arr[hi] = arr[idx]
    arr[idx] = pivot

    return idx


def quick_sort(arr: list[int]) -> None:
    qs(arr=arr, lo=0, hi=len(arr) - 1)
