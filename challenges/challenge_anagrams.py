def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    for char in first_string:
        second_string = second_string.replace(char, '', 1)

    return second_string == ''