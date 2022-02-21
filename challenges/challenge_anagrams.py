def is_anagram(first_string, second_string):
    array = list(second_string)
    try:
        for i in range(len(first_string)):
            array.remove(first_string[i])
        if not array:
            return True
        return False
    except ValueError:
        return False
