# jeito fácil
# def is_palindrome_iterative(word):
#     if word == word[::-1]:
#         return word[::-1]
#     else:
#         return 'false'


def is_palindrome_iterative(word, result='', originalWord=''):
    if not word:
        return False

    if len(originalWord) < len(word):
        originalWord = word

    if(len(word) > 1):
        return is_palindrome_iterative(
            word[0:len(word) - 1],
            result + word[-1],
            originalWord
            )

    if result + word == originalWord:
        return True
    return False


if __name__ == '__main__':
    word = 'REVIVER'
    result = is_palindrome_iterative(word)
    print(result)
