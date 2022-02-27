def is_palindrome_iterative(word):
    test_word = word[::-1]
    if not word:
        return False
    if word == test_word:
        return True
    return False
