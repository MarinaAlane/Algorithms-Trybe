from collections import defaultdict


def array_to_dict(string):
    my_dict = defaultdict(lambda: 0)
    for letter in string:
        my_dict[letter] += 1

    return my_dict


def is_anagram(first_string, second_string):
    return array_to_dict(first_string) == array_to_dict(second_string)
