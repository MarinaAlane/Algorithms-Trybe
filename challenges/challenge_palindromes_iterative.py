def is_palindrome_iterative(word):
    reverse_word = word[-1::-1]

    if not len(word):
        return False
    if word == reverse_word:
        return True
    return False
