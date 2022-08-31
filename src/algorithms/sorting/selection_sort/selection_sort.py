def selection_sort(arr: list[int]) -> list[int]:
    length = len(arr)
    for i in range(length - 1):
        least = i
        for j in range(i + 1, length):
            if arr[j] < arr[least]:
                least = j
        if least != i:
            arr[i], arr[least] = arr[least], arr[i]
    return arr
