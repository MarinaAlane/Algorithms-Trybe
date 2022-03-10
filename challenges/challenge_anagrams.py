def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    if first_string != second_string:
        return False
    return True

# ref https://github.com/tryber/sd-011-project-algorithms/pull/112
