def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    if len(word) == 1:
        return True

    if len(word) == 2:
        return word[low_index] == word[high_index]

    remaining_word = word[low_index+1:high_index]
    check = word[low_index] == word[high_index]

    return check and is_palindrome_recursive(
        remaining_word, 0, len(remaining_word) - 1
    )
