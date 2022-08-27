def binary_search(
    sorted_collection: list[int], wanted_value: int, low: int, high: int
) -> int:
    if high < low:
        return -1

    mid = (low + high) // 2

    if sorted_collection[mid] > wanted_value:
        return binary_search(sorted_collection, wanted_value, low, mid - 1)
    if sorted_collection[mid] < wanted_value:
        return binary_search(sorted_collection, wanted_value, mid + 1, high)
    return mid
