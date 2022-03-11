def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    if low_index >= high_index:
        return True

    letter_1 = word[low_index]
    letter_2 = word[high_index]

    if letter_1 == letter_2:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    return False
