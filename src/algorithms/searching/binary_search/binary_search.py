def binary_search(arr, value):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == value:
            return mid

        if arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1
