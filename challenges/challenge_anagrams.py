def check_anagram(first_string, second_string):
    words = dict()
    if len(first_string) != len(second_string):
        return False

    for i in first_string:
        if i not in words:
            words[i] = 0
            words[i] += 1

    for i in second_string:
        if i not in words:
            return False
        else:
            words[i] -= 1

    for i in words:
        if words[i] > 0 or words[i] < 0:
            return False

    return True


def is_anagram(first_string, second_string):
    if check_anagram(first_string, second_string):
        return True
    else:
        return False
