def is_palindrome_iterative(word):
    if not word:
        return False

    counter = 0

    while counter < len(word) // 2:
        first_current_word = word[counter]
        last_current_word = word[(len(word) - 1) - counter]

        if (first_current_word != last_current_word):
            return False

        counter += 1

    return True

# O range(len(word) // 2) ou o laço for é menos performático?
# Ao substituir por um laço while a performance melhorou de 0.0022 para 0.0018
