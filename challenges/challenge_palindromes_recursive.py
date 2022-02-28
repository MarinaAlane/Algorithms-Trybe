def is_palindrome_recursive(word, low_index, high_index):
    if len(word) > 2 and word[low_index] == word[len(word) - 1]:
        print(word)
        isValid = is_palindrome_recursive(
            word[1: len(word) - 1], 0, len(word) - 1
        )
    elif len(word) == 1 or (
        len(word) == 2 and word[0] == word[1]
    ):
        isValid = True
    else:
        isValid = False

    return isValid
