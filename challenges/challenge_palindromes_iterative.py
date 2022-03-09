def is_palindrome_iterative(word):
    if not word:
        return False
    word_len = len(word) - 1
    for letter in word:
        if letter != word[word_len]:
            return False
        word_len -= 1
    return True
