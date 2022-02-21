def is_palindrome_recursive(word, low_index, high_index):
    if word.strip() == "":
        return False

    return check_palindrome(word, low_index, high_index)


def check_palindrome(word, low_index, high_index):
    if low_index >= high_index:
        return True

    equal_letters = word[low_index] == word[high_index]

    return equal_letters and check_palindrome(
        word, low_index + 1, high_index - 1
    )
