def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not word:
        return False
    if (word[low_index] != word[high_index]):
        return False
    if ((len(word)//2) == low_index):
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
