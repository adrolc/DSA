def binary_search(sorted_collection: list[int], wanted_value: int) -> int:
    low = 0
    high = len(sorted_collection) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_collection[mid] == wanted_value:
            return mid

        if sorted_collection[mid] < wanted_value:
            low = mid + 1
        else:
            high = mid - 1
    return -1
