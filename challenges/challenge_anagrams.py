from challenges.utils import sort


def is_anagram(first_string, second_string):
    if sort(first_string) == sort(second_string):
        return True
    else:
        return False
