def is_palindrome_iterative(word):
    if len(word) < 1:
        return False
    for i in range(len(word) // 2):
        begining_char = word[i]
        end_char = word[-i - 1]
        if begining_char != end_char:
            return False
    return True
