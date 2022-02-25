def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    try:
        l_index, r_index = 0, len(word) - 1

        while l_index < r_index:
            if word[l_index] != word[r_index]:
                return False
            else:
                l_index += 1
                r_index -= 1
        return True
    except ValueError:
        return False
