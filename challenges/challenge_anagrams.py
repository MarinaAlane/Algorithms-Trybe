def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False

    first_sorted = merge_sort([char for char in first_string])
    second_sorted = merge_sort([char for char in second_string])

    return first_sorted == second_sorted


def merge_sort(arr):
    if (len(arr) == 1):
        return arr

    if (len(arr) == 2):
        return arr if arr[0] <= arr[1] else [arr[1], arr[0]]

    middle_index = len(arr) // 2
    left = arr[:middle_index]
    right = arr[middle_index:]
    return merge(merge_sort(left), merge_sort(right))


def merge(arr1, arr2):
    merged = []

    while arr1 or arr2:
        if not arr1:
            merged.extend(arr2)
            break

        if not arr2:
            merged.extend(arr1)
            break

        if (arr2[0] < arr1[0]):
            merged.append(arr2.pop(0))
        else:
            merged.append(arr1.pop(0))

    return merged
