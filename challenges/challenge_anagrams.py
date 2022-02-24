# def merge_sort(array):
#     if len(array) <= 1:
#         return array
#     mid = len(array) // 2

#     left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
#     return merge(left, right, array.copy())


# def merge(left, right, merged):
#     left_cursor, right_cursor = 0, 0
#     while left_cursor < len(left) and right_cursor < len(right):
#         if left[left_cursor] <= right[right_cursor]:
#             merged[left_cursor + right_cursor] = left[left_cursor]
#             left_cursor += 1
#         else:
#             merged[left_cursor + right_cursor] = right[right_cursor]
#             right_cursor += 1
#     for left_cursor in range(left_cursor, len(left)):
#         merged[left_cursor + right_cursor] = left[left_cursor]
#     for right_cursor in range(right_cursor, len(right)):
#         merged[left_cursor + right_cursor] = right[right_cursor]

#     return merged


def quicksort(array, low, high):
    if len(array) == 1:
        return array

    if low < high:
        partition_index = partition(array, low, high)
        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)


def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):

        if array[j] <= pivot:

            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    if not first_string or not second_string:
        return False
    elif len(first_string) != len(second_string):
        return False
    first_str_ordered = list(first_string)
    quicksort(first_str_ordered, 0, len(first_string) - 1)
    second_str_ordered = list(second_string)
    quicksort(second_str_ordered, 0, len(second_string) - 1)

    if first_str_ordered == second_str_ordered:
        return True
    else:
        return False
