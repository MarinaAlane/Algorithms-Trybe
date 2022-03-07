def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    for value in first_string:
        second_string = second_string.replace(value, '', 1)
    return len(second_string) == 0
