def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    if word[low_index] == word[high_index]:
        if low_index < high_index:
            new_low_index = low_index + 1
            new_high_index = high_index - 1
            return is_palindrome_recursive(word, new_low_index, new_high_index)
        else:
            return True
    else:
        return False
