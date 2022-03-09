def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False
    palindrome = word[low_index] is word[high_index]
    if palindrome:
        if low_index < high_index:
            low_index += 1
            high_index -= 1
            return is_palindrome_recursive(word, low_index , high_index)
        return True
    else:
        return False
