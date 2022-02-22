from challenges.utils.custom_reverce import custom_reverce


def is_palindrome_recursive(word, low_index, high_index):
    if len(word) < 1:
        return False
    palindrome = custom_reverce(word, low_index, high_index)
    return palindrome == word
