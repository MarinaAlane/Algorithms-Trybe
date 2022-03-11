def is_palindrome_iterative(word):

    if not word:
        return False
    if str(word) == str(word)[::-1]: # o indice comeca do final e vai ate o inicio decrementando 1
        return True
    else:
        return False
