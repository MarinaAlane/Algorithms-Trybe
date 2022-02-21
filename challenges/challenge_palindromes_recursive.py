def is_palindrome_recursive(word, low_index, high_index):
    try:
        if low_index >= high_index and len(word) > 0:
            return True
        if len(word) == 0 or word[low_index] != word[high_index]:
            return False
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    except TypeError:
        return False
        
# rerun
