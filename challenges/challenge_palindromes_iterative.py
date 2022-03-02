def is_palindrome_iterative(word):
    if word is None or word == '':
        return False

    is_palindrome = True
    for index, letter in enumerate(word):
        if letter != word[-(index+1)]:
            return False

    return is_palindrome
