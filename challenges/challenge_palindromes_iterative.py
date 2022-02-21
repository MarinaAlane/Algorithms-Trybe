def is_palindrome_iterative(word):
    if len(word) < 1:
        return False

    left_index = 0
    right_index = len(word) - 1
    is_palindrome = True

    while left_index <= right_index:
        if word[left_index] != word[right_index]:
            is_palindrome = False
            break

        left_index += 1
        right_index -= 1

    return is_palindrome
