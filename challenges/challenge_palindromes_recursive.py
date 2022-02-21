def is_palindrome_recursive(word, low_index, high_index):
    # if word == "":
    #     return False

    if len(word) <= 1:
        return True
    lenght = len(word) - 1
    if word[0] == word[lenght]:

        return is_palindrome_recursive(word[1:lenght], 0, lenght)
    else:

        return False


# def is_palindrome_recursive(word, low_index, high_index):
#     if word == "":
#         return False

#     lenght = len(word) - 1
#     if word[0] != word[lenght]:
#         return False
#     else:
#         if len(word) >= 1:
#             return is_palindrome_recursive(word[1:lenght], 0, lenght)
#         return True
