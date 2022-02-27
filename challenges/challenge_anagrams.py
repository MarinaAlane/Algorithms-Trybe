def create_dict(word):
    """ Faça o código aqui. """
    dict_ = {}
    for letter in word:
        if letter in dict_:
            dict_[letter] += 1
        else:
            dict_[letter] = 1
    return dict_


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    dict1 = create_dict(first_string)
    dict2 = create_dict(second_string)
    if len(dict1) != len(dict2):
        return False
    for key in dict1:
        if key in dict2:
            if dict1[key] != dict2[key]:
                return False
        else:
            return False
    return True
