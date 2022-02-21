def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    for letter in first_string:
        if letter not in second_string:
            return False
        second_string = second_string.replace(letter, "", 1)
    return True