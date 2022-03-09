def is_palindrome_recursive(word, low_index, high_index):
    if not word or word[low_index] != word[high_index]:
        return False

    if high_index - low_index <= 0:
        return True

    next_initial_char = low_index + 1
    previous_last_char = high_index - 1

    return is_palindrome_recursive(word, next_initial_char, previous_last_char)

