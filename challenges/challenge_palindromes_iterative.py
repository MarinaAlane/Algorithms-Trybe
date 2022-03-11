import math


def is_palindrome_iterative(word):

    if word == "":
        return False

    length = len(word)
    middle = math.ceil(length / 2)

    for i in range(0, middle):
        if word[i] != word[(length - 1) - i]:
            return False

    return True
