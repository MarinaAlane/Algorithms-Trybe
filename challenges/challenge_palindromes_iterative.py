def is_palindrome_iterative(word):
    if word == "":
        return False

    high = len(word) - 1
    low = 0

    while low < high:
        if word[low] != word[high]:
            return False
        low += 1
        high -= 1

    return True
