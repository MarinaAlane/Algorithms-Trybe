def merge(left, right):
    string = [*left, *right]
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            string[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            string[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        string[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        string[left_cursor + right_cursor] = right[right_cursor]
    return string


def merge_sort_string(string):
    if len(string) <= 1:
        return string
    mid = len(string) // 2
    left = merge_sort_string(string[:mid])
    right = merge_sort_string(string[mid:])
    return merge(left, right)


def is_anagram(first_string, second_string):
    first_sorted_string = merge_sort_string(first_string)
    second_sorted_string = merge_sort_string(second_string)
    return first_sorted_string == second_sorted_string
