def is_palindrome_recursive(word, low_index, high_index):
    if word == '' or (word[low_index] != word[high_index]):
        return False
    elif len(word) > 0 and low_index >= high_index:
        return True
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
