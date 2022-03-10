# reference https://www.w3resource.com/python-exercises
# /python-functions-exercise-12.php

def is_palindrome_recursive(word, low_index, high_index):
    try:
        if (low_index - high_index) < 2:
            return is_palindrome(word, low_index, high_index)
        return True
    except IndexError:
        return False


def is_palindrome(word, low_index, high_index):
    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index+1, high_index-1)
    else:
        return False
