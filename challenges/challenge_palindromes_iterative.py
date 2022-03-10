def is_palindrome_iterative(word):
    if not word:
        return False
    right = len(word) - 1
    left = 0

    while left < right:
        if word[left] == word[right]:
            right = right - 1
            left = left + 1
        else:
            return False

    return True
