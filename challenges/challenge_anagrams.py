def get_char_count(string):
    char_count = dict()

    for char in string:
        try:
            char_count[char] += 1
        except KeyError:
            char_count[char] = 1

    return char_count


def is_anagram(first_string, second_string):
    return get_char_count(first_string) == get_char_count(second_string)