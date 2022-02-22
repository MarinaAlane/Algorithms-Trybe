def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    checker = ''
    if len(word) < 1:
        return False
    elif len(word) == 1:
        return True
    for i in range(len(word)//2):
        if word[i] == word[-i - 1]:
            checker = True
        else:
            checker = False
    return checker
