def is_palindrome_iterative(word):
    if not word:
        return False

    reverse = word[::-1]

    return word == reverse
