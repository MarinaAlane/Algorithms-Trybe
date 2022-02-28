def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    aux_string = second_string
    for char in first_string:
        if char in aux_string:
            aux_string = aux_string.replace(char, '', 1)
    return True if len(aux_string) == 0 else False
