from challenges.utils.custom_sort import custom_sort


def is_anagram(first_string, second_string):
    if len(first_string) is not len(second_string):
        return False
    first_string = "".join(custom_sort(first_string))
    second_string = "".join(custom_sort(second_string))
    return first_string == second_string
