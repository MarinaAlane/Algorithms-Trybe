def is_palindrome_iterative(word):
    if not word:
        return False
    check_palindrome = "".join(char.lower() for char in word if char.isalnum())
    return check_palindrome == check_palindrome[::-1]
# Code based in this article:
# https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Problems/Palindrome.html
