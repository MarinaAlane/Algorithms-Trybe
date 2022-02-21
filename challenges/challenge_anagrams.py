import timeit


def merge(left, right, char_list):

    left_index, right_index = 0, 0
    full_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            char_list[full_index] = left[left_index]
            left_index += 1
        else:
            char_list[full_index] = right[right_index]
            right_index += 1
        full_index += 1

    while left_index < len(left):
        char_list[full_index] = left[left_index]
        left_index += 1
        full_index += 1

    while right_index < len(right):
        char_list[full_index] = right[right_index]
        right_index += 1
        full_index += 1

    return char_list


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
    setup_import = "from challenges.challenge_anagrams " "import is_anagram"
    time = timeit.timeit(
        'is_anagram("amora", "aroma")',
        setup=f"{setup_import}",
        number=1000,
    )
    print(time)
