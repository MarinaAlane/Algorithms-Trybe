def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    elif low_index >= high_index:
        return word == word[::-1]
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
