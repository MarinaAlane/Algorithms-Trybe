def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    if low_index == high_index:
        return True
    if high_index - low_index == 1:
        return word[low_index] == word[high_index]

    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
