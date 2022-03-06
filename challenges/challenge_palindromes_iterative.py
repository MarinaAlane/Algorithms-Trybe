def is_palindrome_iterative(word):
    if (len(word) == 0):
        return False

    for index in range(len(word) // 2):
        first_current_word = word[index]
        last_current_word = word[(len(word) - 1) - index]

        if(first_current_word != last_current_word):
            return False

    return True
