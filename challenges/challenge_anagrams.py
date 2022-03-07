def mount_dict(string):
    dictio = dict()
    for letter in string:
        try:
            dictio[letter] += 1
        except KeyError:
            dictio[letter] = 1

    return dictio


def is_anagram(first_string, second_string):
    dict_1 = mount_dict(first_string)
    dict_2 = mount_dict(second_string)

    return dict_1 == dict_2
