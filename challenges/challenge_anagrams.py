def char_counter(string):
    counted_char = {}
    for char in string:
        if char in counted_char:
            counted_char[char] += 1
        else:
            counted_char[char] = 1
    return counted_char


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first_string_counted = char_counter(first_string)
    second_string_counted = char_counter(second_string)

    return first_string_counted == second_string_counted
