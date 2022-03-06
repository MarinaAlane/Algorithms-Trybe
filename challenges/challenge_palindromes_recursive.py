def is_palindrome_recursive(word, low_index, high_index):
    if len(word) < 1:
        return False
    palindrome = reverse(word, low_index, high_index)
    return palindrome == word


def reverse(word, low_index, high_index):
    if low_index == high_index:
        return word
    return (
        reverse(word[1:], low_index, len(word[1:]) - 1)
        + word[0]
    )
