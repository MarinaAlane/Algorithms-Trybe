def is_anagram(first_string, second_string):
    try:
        second_string = list(second_string)

        for num in range(len(first_string)):
            second_string.remove(first_string[num])

        if not second_string:
            return True

        return False
    except ValueError:
        return False
