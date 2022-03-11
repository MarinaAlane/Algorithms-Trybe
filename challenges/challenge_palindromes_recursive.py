def is_palindrome_recursive(w, low_index, high_index):
    if w == "" or w[low_index] != w[high_index]:
        return False
    if low_index >= high_index:
        return True
    return is_palindrome_recursive(w, low_index + 1, high_index - 1)
