def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if word == "":
        return False
    elif len(word) <= 1:
        return True
    else:
        return word[low_index] == word[high_index] and is_palindrome_recursive(
            word[1 : len(word) - 1], 0, len(word) - 1
        )


def test(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and test(word[1 : len(word) - 1])
