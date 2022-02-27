import math


def is_palindrome_iterative(word):
    half = math.floor(len(word) / 2)
    counter = 0
    while counter <= half:
        try:
            if word[counter] != word[len(word) - 1 - counter]:
                return False
            counter += 1
        except IndexError:
            return False
    return True
