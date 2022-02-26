def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    try:
        if not word or word[low_index] != word[high_index]:
            return False
        elif low_index >= high_index:
            return word[low_index] == word[high_index]
        else:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    
    except TypeError:
        return False