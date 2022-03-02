def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    if high_index - low_index < 1:
        return True

    if word[low_index] == word[high_index]:
        next_low_index, next_high_index = low_index + 1, high_index - 1
        return is_palindrome_recursive(word, next_low_index, next_high_index)

    return False
