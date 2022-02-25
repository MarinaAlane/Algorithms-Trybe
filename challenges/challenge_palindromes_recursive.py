
def is_palindrome_recursive(word, low_index, high_index):

    if word == "":
        return False

    if word[low_index] != word[high_index]:
        return False
    if high_index <= (len(word) - 1) / 2:
        return True

    return (True
            and is_palindrome_recursive(word, low_index + 1, high_index - 1))