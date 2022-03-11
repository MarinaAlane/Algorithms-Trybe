def is_palindrome_iterative(word):
    palin = []

    if(len(word) == 0):
        return False
    for letter in word:
        palin.insert(0, letter)
    return ''.join(palin) == word
