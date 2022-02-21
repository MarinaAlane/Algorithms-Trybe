def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False

    first_sorted = merge_sort(get_chars(first_string))
    second_sorted = merge_sort(get_chars(second_string))

    return first_sorted == second_sorted


def get_chars(string):
    return [char for char in string]


def merge_sort(arr):
    if (len(arr) == 1):
        return arr

    if (len(arr) == 2):
        return sort_list_with_two_elements(arr)

    middle_index = len(arr) // 2
    left = arr[:middle_index]
    right = arr[middle_index:]
    return merge(merge_sort(left), merge_sort(right), [])


def sort_list_with_two_elements(arr):
    return arr if arr[0] <= arr[1] else [arr[1], arr[0]]


def merge(arr1, arr2, merged):
    if len(arr1) == 0 and len(arr2) == 0:
        return merged

    if len(arr1) == 0:
        merged.extend(arr2)
        return merged

    if len(arr2) == 0:
        merged.extend(arr1)
        return merged

    if (arr1[0] < arr2[0]):
        merged.append(arr1.pop(0))
    else:
        merged.append(arr2.pop(0))

    return merge(arr1, arr2, merged)
