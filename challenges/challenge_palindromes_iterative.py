def is_palindrome_iterative(word):
    if word == '':
        return False
    else:
        return word == word[::-1]
