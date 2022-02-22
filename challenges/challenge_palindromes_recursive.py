def is_palindrome_recursive(word, low_index=0, high_index=-1):
    """ Faça o código aqui. """
    if type(word) is not str or not word:
        return False

    if word[low_index] != word[high_index]:
        return False

    low_index += 1
    high_index += -1

    if low_index == len(word):
        return True
    else:
        return is_palindrome_recursive(word, low_index, high_index)
