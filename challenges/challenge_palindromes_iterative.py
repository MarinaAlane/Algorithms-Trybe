def is_palindrome_iterative(word):
    if not word:
        return False
    for index, letter in enumerate(word):
        if word[-index - 1] != letter:
            return False
    return True


if __name__ == '__main__':
    word = 'ama'
    result = is_palindrome_iterative(word)
    print(result)
