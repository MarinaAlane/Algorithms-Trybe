def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    for element in first_string:
        if element in second_string:
            second_string = second_string.replace(element, '', 1)

    return len(second_string) == 0
