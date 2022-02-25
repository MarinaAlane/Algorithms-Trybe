from operator import truediv


def check_anagram(first_string, second_string):
    """ Faça o código aqui. """
    anagram = dict()
    if len(first_string) != len(second_string):
        return False

    for i in first_string:
        if i not in anagram:
            anagram[i] = 0
            anagram[i] += 1

    for i in second_string:
        if i not in anagram:
            return False
        else:
            anagram[i] -= 1

    for i in anagram:
        if anagram[i] > 0 or anagram[i] < 0:
            return False

    return True


def is_anagram(first_string, second_string):
    if check_anagram(first_string, second_string):
        return True
    else:
        return False
