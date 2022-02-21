def is_palindrome_recursive(word, low_index, high_index):
    try:
        low_char, high_char = word[low_index], word[high_index]
        sliced_word = word[1:-1]
        if low_char != high_char:
            return False
        if len(word) < 2 or (len(word) == 2 and word[0] == word[1]):
            return True
        return is_palindrome_recursive(sliced_word, 0, len(sliced_word) - 1)
    except IndexError:
        return False
