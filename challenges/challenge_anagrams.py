def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    second_string = list(second_string)

    try:
        for l in range(len(first_string)):
            second_string.remove(first_string[l])

        if not second_string:
            return True

        return False
    except ValueError:
        return False
