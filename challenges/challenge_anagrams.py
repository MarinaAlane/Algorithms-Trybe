def is_anagram(first_string, second_string):
    second_string_array = list(second_string)
    try:
        for i in range(len(first_string)):
            second_string_array.remove(first_string[i])
        if len(second_string_array) == 0:
            return True
        return False
    except ValueError:
        return False


is_anagram('amor', 'roma')
