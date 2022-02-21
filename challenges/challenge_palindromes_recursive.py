def is_palindrome_recursive(word, low_index = 0, high_index = 0):
    """ Faça o código aqui. """
    if high_index == -1:
        return False
    elif len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome_recursive(word[1:-1])
