from challenges.merge_sort import merge_sort


def is_anagram(first_string, second_string):
    first_string_array = merge_sort(list(first_string))
    second_string_array = merge_sort(list(second_string))

    return first_string_array == second_string_array
