def is_palindrome_recursive(word, low_index, high_index):
    try:
        if (word[low_index] != word[high_index] or len(word) == 0):
            return False
        if (low_index >= high_index or len(word) < 0):
            return True
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    except (TypeError, IndexError):
        return False
    """ Faça o código aqui. """
