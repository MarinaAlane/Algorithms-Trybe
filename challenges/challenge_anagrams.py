def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    for letter in first_string:
        if letter in second_string:
            second_string = second_string.replace(letter, '', 1)

    if len(second_string) == 0:
        return True
    else:
        return False

# Ref:
# https://appdividend.com/2020/01/21/python-list-contains-how-to-check-if-item-exists-in-list/
