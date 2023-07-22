# Bubble sort
# Time complexity: O(n^2)


def bubble_sort(arr):
    # bubble inspects the first element and checks if it is bigger
    # than the next.
    # if the inspected is bigger then it is swapped with the next.
    # The next is then inspected.
    # After each iteration the biggest element arrives at the last
    # index of the list
    # We iterate over the array moving the largest number
    # encountered to the end, excluding the previous biggest

    search_lenght = len(arr) - 1
    for i in range(len(arr)):
        for j in range(search_lenght - i):
            print(arr)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # arr = [3, 4, 7, 9, 42, 69, 420];
