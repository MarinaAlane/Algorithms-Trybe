def is_anagram(first_string, second_string):
    dict_1 = dict()
    dict_2 = dict()
    for letter in first_string:
        try:
            dict_1[letter] += 1
        except KeyError:
            dict_1[letter] = 1

    for letter in second_string:
        try:
            dict_2[letter] += 1
        except KeyError:
            dict_2[letter] = 1

    return dict_1 == dict_2
