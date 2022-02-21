import math


def is_palindrome_recursive(word, low_index, high_index):
    if word == '' or word[low_index] != word[high_index]:
        return False

    if low_index >= high_index:
        return True

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


# print(is_palindrome_recursive('GG', 0, 1))
# print(is_palindrome_recursive('GGG', 0, 2))
# print(is_palindrome_recursive('GOOG', 0, 3))
# print(is_palindrome_recursive('GOGOG', 0, 4))
print(is_palindrome_recursive('GOGGOG', 0, 5))
