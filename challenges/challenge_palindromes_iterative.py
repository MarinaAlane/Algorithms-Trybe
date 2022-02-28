def is_palindrome_iterative(word):
    if (len(word) == 0):
        return False

    if (word[:: 1] == word[:: -1]):
        return True
    else:
        return False
