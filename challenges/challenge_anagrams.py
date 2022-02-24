def character_counter(string):
    character_dict = dict()

    for char in string:
        if (char in character_dict):
            character_dict[char] += 1
        else:
            character_dict[char] = 1

    return character_dict


def is_anagram(first_string, second_string):
    if (len(first_string) != len(second_string)):
        return False

    character_dict = character_counter(first_string + second_string)

    for value in character_dict.values():
        if (value % 2 != 0):
            return False

    return True
