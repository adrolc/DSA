def merge_sort(arr):
    if not arr:
        return arr
    length = len(arr)
    mid = length // 2

    if length == 1:
        return arr

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    combined = []
    len_left = len(left)
    len_right = len(right)
    left_index = right_index = 0

    while left_index < len_left and right_index < len_right:
        if left[left_index] > right[right_index]:
            combined.append(right[right_index])
            right_index += 1
        else:
            combined.append(left[left_index])
            left_index += 1

    while left_index < len_left:
        combined.append(left[left_index])
        left_index += 1

    while right_index < len_right:
        combined.append(right[right_index])
        right_index += 1

    return combined
