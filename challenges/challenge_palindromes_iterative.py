def is_palindrome_iterative(word):
    if word == "":
        return False
    reverse_word = word[::-1]
    return reverse_word == word
