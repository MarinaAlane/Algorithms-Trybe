def is_palindrome_iterative(word):
    if not word:
        return False

    repetition = 0
    index = 0

    while repetition < len(word) // 2:
        reversed_index = -1 * (index + 1)

        if word[index] != word[reversed_index]:
            return False

        repetition += 1
        index += 1

    return True
