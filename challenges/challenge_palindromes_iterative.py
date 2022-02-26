def is_palindrome_iterative(word):
    if not word:
        return False
# https://www.youtube.com/watch?v=5VBWe6BXzRo
    return word == word[::-1]
