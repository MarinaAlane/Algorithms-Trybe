# code export in the https://stackoverflow.com/questions/61604504/palindrome
# -iterative-checker-in-python

def is_palindrome_iterative(word):
    for forward, backward in zip(word, reversed(word)):
        if forward != backward:
            return False
    return True
