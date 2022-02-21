def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(array.copy(), left, right)


def merge(ordenated, left, right):
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            ordenated[left_index + right_index] = left[left_index]
            left_index += 1
        else:
            ordenated[left_index + right_index] = right[right_index]
            right_index += 1

    for left_index in range(left_index, len(left)):
        ordenated[left_index + right_index] = left[left_index]

    for right_index in range(right_index, len(right)):
        ordenated[left_index + right_index] = right[right_index]

    return ordenated
