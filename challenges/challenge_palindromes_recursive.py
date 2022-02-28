# jeito fácil
# def is_palindrome_recursive(word):
#     if word == word[::-1]:
#         return word[::-1]
#     else:
#         return 'false'


# def is_palindrome_recursive(word, low_index, high_index):
# Mudei os parametros porque eu fiz a recursiva na iterativa e lá não
# mostrava todos os parametros
# Por isso criei os paremetros láa e quando vi estavam diferentes kkk
# Mas não passa no avaliador kkk
# def is_palindrome_recursive(word, result='', originalWord=''):
#     if not word:
#         return False

#     if len(originalWord) < len(word):
#         originalWord = word

#     if(len(word) > 1):
#         return is_palindrome_recursive(
#             word[0:len(word) - 1],
#             result + word[-1],
#             originalWord
#             )

#     if result + word == originalWord:
#         return True
#     return False

def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if low_index == high_index:
        return True

    if word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


if __name__ == '__main__':
    word = 'edu'
    result = is_palindrome_recursive(word, 0, len(word) - 1)
    print(result)
