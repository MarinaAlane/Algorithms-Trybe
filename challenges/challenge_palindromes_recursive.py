def is_palindrome_recursive(word, low_index, high_index):
    try:
        if len(word) == 0:
            return False
        if low_index >= len(word):
            return True
        return (
            word[low_index] == word[high_index]
            and is_palindrome_recursive(word, low_index + 1, high_index - 1))

    except ValueError:
        return False
