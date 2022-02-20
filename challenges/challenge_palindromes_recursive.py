def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 1:
        return True
    elif len(word) == 2 and word[low_index] == word[high_index]:
        return True
    elif word == "" or word[low_index] != word[high_index]:
        return False
    else:
        sliced_word = word[1:high_index]
        return is_palindrome_recursive(sliced_word, 0, len(sliced_word) - 1)
