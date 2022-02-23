def is_palindrome_iterative(word):
    is_palindrome = False
    if len(word) > 0 and word == str(word)[::-1]:
        return True
    return is_palindrome
