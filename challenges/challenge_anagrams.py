def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first_string = first_string.lower()
    second_string = second_string.lower()

    first_string_list = list(first_string)
    second_string_list = list(second_string)

    for letter in first_string_list:
        if letter in second_string_list:
            second_string_list.remove(letter)
        else:
            return False

    return True
