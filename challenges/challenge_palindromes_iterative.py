def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    first_index = 0
    last_index = -1
    mid = len(word) // 2
    while first_index < mid:
        if word[first_index] != word[last_index]:
            return False
        first_index += 1
        last_index -= 1
    return True
