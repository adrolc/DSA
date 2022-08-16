def bubble_sort(arr):
    length = len(arr)
    bound = length - 1
    for _ in range(length):
        swapped = False
        for j in range(bound):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                bound = j
        if not swapped:
            break
    return arr