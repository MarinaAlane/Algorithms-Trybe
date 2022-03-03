def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    elif low_index > len(word) - 1:
        return True

    if (word[low_index] == word[high_index]):
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return False
