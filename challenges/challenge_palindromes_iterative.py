def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if not word:
        return False
    else:
        return word == word[::-1]
