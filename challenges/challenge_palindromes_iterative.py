def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    if len(word) == 1:
        return True
    l_index = 0
    r_index = len(word) - 1

    while l_index < r_index:
        if word[l_index] != word[r_index]:
            return False
        else:
            l_index += 1
            r_index -= 1
    return True
