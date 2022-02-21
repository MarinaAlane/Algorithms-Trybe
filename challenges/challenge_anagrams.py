def set_string(string, character_dict, method=-1):
    for i in string:
        if i in character_dict:
            character_dict[i] += method
        else:
            character_dict[i] = 1
    return character_dict


def is_anagram(first_string, second_string):
    character_dict = dict()

    character_dict = set_string(first_string, character_dict, 1)
    character_dict = set_string(second_string, character_dict)

    for i in character_dict:
        if character_dict[i] != 0:
            return False
    return True
