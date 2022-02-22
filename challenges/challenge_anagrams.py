def create_dict(first_string):
    dict = {}
    for letter in first_string:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict


def is_anagram(first_string, second_string):
    dict = {}
    dict = create_dict(first_string)
    for letter in second_string:
        if letter in dict:
            dict[letter] -= 1
        else:
            return False
    for letter in dict:
        if dict[letter] != 0:
            return False
    return True
