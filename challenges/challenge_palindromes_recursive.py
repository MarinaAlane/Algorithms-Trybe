# https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/


def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if len(word) < 1:
        return False
    elif low_index == high_index:
        return True
    elif word[low_index] != word[high_index]:
        return False
    elif low_index < high_index + 1:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return True
