def is_palindrome_iterative(word):
    if len(word) > 0 and word == str(word)[::-1]:
        return True
    return False
