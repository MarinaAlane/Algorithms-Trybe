def is_anagram(first_string, second_string):
    return word_dict(first_string) == word_dict(second_string)


def word_dict(word):
    word_dict = dict()

    for character in word:
        if word_dict.get(character) is None:
            word_dict[character] = 1
        else:
            word_dict[character] += 1

    return word_dict
