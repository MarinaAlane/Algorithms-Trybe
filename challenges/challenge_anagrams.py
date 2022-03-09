def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    for e in first_string:
        if first_string.count(e) != second_string.count(e):
            return False
    return True
