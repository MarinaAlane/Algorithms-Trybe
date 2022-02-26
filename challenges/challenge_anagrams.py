def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    first_word = dict()
    second_word = dict()

    for letter in first_string:
        if first_word.get(letter) is None:
            first_word[letter] = 1
        else:
            first_word[letter] += 1
    
    for letter in second_string:
        if second_word.get(letter) is None:
            second_word[letter] = 1
        else:
            second_word[letter] += 1

    return first_word == second_word