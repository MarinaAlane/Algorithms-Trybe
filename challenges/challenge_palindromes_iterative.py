def is_palindrome_iterative(word):
    if not word:
        return False

    counter = 0
    result = True

    while counter <= (len(word) // 2) - 1:
        result = word[counter] == word[-counter - 1]
        counter += 1

    return result
