def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):

        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return ''.join(merged)


def merge_sort(string):
    if len(string) <= 1:
        return string
    mid = len(string) // 2
    left, right = merge_sort(string[:mid]), merge_sort(string[mid:])
    return merge(left, right, string)


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if 0 in (len(first_string), len(second_string)):
        return False

    first_sorted = merge_sort(list(first_string))
    second_sorted = merge_sort(list(second_string))
    return first_sorted == second_sorted


if __name__ == '__main__':
    print(is_anagram('amor', 'roma'))
