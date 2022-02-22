from challenges.utils.custom_reverse import custom_reverse


def is_palindrome_recursive(word, low_index, high_index):
    if len(word) < 1:
        return False
    palindrome = custom_reverse(word, low_index, high_index)
    return palindrome == word
