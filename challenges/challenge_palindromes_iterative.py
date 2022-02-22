def is_palindrome_iterative(word):
    if word == '':
        return False

    max_iterator = len(word) // 2
    max_index = len(word) - 1

    for i in range(max_iterator):
        if word[i] != word[max_index - i]:
            return False

    return True
