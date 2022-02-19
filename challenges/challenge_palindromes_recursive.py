def is_palindrome_recursive(word, low_index, high_index):
    length = len(word)
    if(length == 0 or word[low_index] != word[high_index]):
        return False
    if(((high_index - 1) - (low_index + 1)) < 1):
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
