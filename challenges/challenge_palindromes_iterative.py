def is_palindrome_iterative(word):
    if word == "":
        return False
    return word == word[::-1]


# https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/

# def is_palindrome_iterative(word):
#     if len(word) == 0:
#         return False
#     length = int(len(word))
#     for index in range(0, length // 2):
#         if word[index] != str(len(word) - index - 1):
#             return False
#         return True
