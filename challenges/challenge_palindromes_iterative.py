def is_palindrome_iterative(word):
    if word == "":
        return False
    reversed_word = ''.join(reversed(word))
    if(word == reversed_word):
        return True
    else:
        return False
