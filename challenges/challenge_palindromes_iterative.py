# code export in the https://stackoverflow.com/questions/61604504/palindrome
# -iterative-checker-in-python
# reference pull 139 

def is_palindrome_iterative(word):
    # for forward, backward in zip(word, reversed(word)):
    #     if forward != backward:
    #         return False
    # return True
    if word == '':
        return False

    return word == word[::-1]
