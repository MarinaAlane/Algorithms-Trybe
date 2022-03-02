def is_palindrome_iterative(word):
    if word == '':
        return False

    for index, letter in enumerate(word):
        if letter != word[-(index+1)]:
            return False

    return True
