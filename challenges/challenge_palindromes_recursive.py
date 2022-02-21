def utils_palindrome_recursive(word, low_index, high_index):
    if low_index == high_index:
        return word
    return (
        utils_palindrome_recursive(word[1:], low_index, len(word[1:]) - 1)
        + word[0]
    )


def is_palindrome_recursive(word, low_index, high_index):
    if len(word) < 1:
        return False
    palindrome = utils_palindrome_recursive(word, low_index, high_index)
    return palindrome == word
