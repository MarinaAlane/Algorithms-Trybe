def is_palindrome_iterative(word):
    result = ""
    if len(word) == 0:
        return False
    for number in reversed(word):
        result += number
    return result == word
