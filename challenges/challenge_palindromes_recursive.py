def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if len(word) == 1:
        return True
    if low_index <= high_index:
        return word[low_index] == word[high_index] and is_palindrome_recursive(
            word, low_index + 1, high_index - 1
        )
    return word[low_index] == word[high_index]
