def binary_search(arr, value, low, high):
    if high < low:
        return -1

    mid = (low + high) // 2

    if arr[mid] > value:
        return binary_search(arr, value, low, mid - 1)
    if arr[mid] < value:
        return binary_search(arr, value, mid + 1, high)
    return mid
