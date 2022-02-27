def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    anagram = second_string
    for leather in first_string:
        if leather in anagram:
            anagram = anagram.replace(leather, "", 1)

    if len(anagram) == 0:
        return True

    return False
