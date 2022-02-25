def merge_sort(data):
    if len(data) <= 1:
        return data

    m = len(data) // 2

    left, right = merge_sort(data[m:]), merge_sort(data[:m])

    return merge(left, right, data.copy())


def merge(left, right, data):
    l_index, r_index = 0, 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            data[l_index + r_index] = left[l_index]
            l_index += 1
        else:
            data[l_index + r_index] = right[r_index]
            r_index += 1
    for l_index in range(l_index, len(left)):
        data[l_index + r_index] = left[l_index]

    for r_index in range(r_index, len(right)):
        data[l_index + r_index] = right[r_index]
    return data


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first = merge_sort(list(first_string).copy())
    second = merge_sort(list(second_string).copy())

    if first == second:
        return True
    else:
        return False
