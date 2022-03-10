def is_palindrome_iterative(word):
    if not word:
        return False
    reverse_word = ""
    for i in word:
        reverse_word = i + reverse_word
    if word == reverse_word:
        return True
    else:
        return False
