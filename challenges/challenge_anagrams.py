def is_anagram(first_string, second_string):
    same_len = len(first_string) == len(second_string)

    if not first_string or not second_string or not same_len:
        return False

    first_array = list(first_string)
    second_array = list(second_string)

    try:
        for letter in first_array:
            second_array.remove(letter)
    except ValueError:
        return False

    return not len(second_array)
