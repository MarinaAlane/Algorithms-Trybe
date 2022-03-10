def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    first_phrase = invert_word(first_string)
    second_phrase = invert_word(second_string)
    for i in range(len(first_phrase)):
        if first_phrase[i] == second_phrase[i]:
            return True
        else:
            return False


# codigo extraido dos exercicios do course
# onde exercemos um algoritmo de força bruta
# conseguindo criar nossa proprio sort


def invert_word(phrase):
    word_array = []
    for letter in phrase:
        word_array.append(letter)
    for i in range(len(word_array)):
        minimum = i
        for j in range(i + 1, len(word_array)):
            if word_array[j] < word_array[minimum]:
                minimum = j
    word_array[minimum], word_array[i] = word_array[i], word_array[minimum]
    return word_array
