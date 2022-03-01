def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    for each_letter in first_string:
        if each_letter in second_string:
            second_string = second_string.replace(each_letter, '', 1)
    if len(second_string) == 0:
        return True

    return False
