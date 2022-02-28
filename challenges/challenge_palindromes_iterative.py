def is_palindrome_iterative(word):
    if not word:
        return False

    reversed = ''

    for index in range(len(word) - 1, -1, -1):
        reversed += word[index]

    return reversed == word
