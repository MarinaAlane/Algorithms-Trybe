from .helper.merge_sort import merge_sort


def is_anagram(first_string, second_string):
    first_string = merge_sort(list(first_string))
    second_string = merge_sort(list(second_string))
    return first_string == second_string
