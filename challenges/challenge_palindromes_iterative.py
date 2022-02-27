def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if word == "":
        return False
    lower_index = 0
    high_index = len(word) - 1

    while lower_index < high_index:
        if word[lower_index] != word[high_index]:
            return False
        lower_index += 1
        high_index -= 1
    return True
