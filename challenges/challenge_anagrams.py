from collections import defaultdict


def is_anagram(first_string, second_string):
    first_string_dict = defaultdict(lambda: 0)
    second_string_dict = defaultdict(lambda: 0)
    for letter in first_string:
        first_string_dict[letter] += 1
    for letter in second_string:
        second_string_dict[letter] += 1

    return first_string_dict == second_string_dict
