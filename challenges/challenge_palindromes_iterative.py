# def is_palindrome_iterative(word):
#     is_palindrome = True
#     half_index = len(word) // 2
#     index = 0
#     if not word:
#         is_palindrome = False
#     while is_palindrome and index <= half_index:
#         if word[index] != word[-index - 1]:
#             is_palindrome = False
#         else:
#             index += 1
#     return is_palindrome

# src:
# https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/


def is_palindrome_iterative(word):
    if not word:
        return False
    return word == word[::-1]
