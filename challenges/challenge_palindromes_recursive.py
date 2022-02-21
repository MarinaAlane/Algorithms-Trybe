def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    # low_index = 0 high_index = len(word - 1)
    if word == ' ' or len(word) < 1:
        return False
    if len(word) == 1 or low_index == len(word) + 1 or high_index == 0:
        return True
    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, (low_index + 1), (high_index - 1))
    else:
        return False
