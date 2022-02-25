from helpers.sort import sort


def is_anagram(first_string, second_string):

    if sort(first_string) == sort(second_string):
        return True

    if not first_string or not second_string:
        return False

    if len(first_string) != len(second_string):
        return False

    return False
