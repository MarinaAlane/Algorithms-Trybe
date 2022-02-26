def create_dict_from_string(string):
    string_dict = {}
    for letter in string:
        if letter in string_dict:
            string_dict[letter] += 1
        else:
            string_dict[letter] = 1

    return string_dict


def is_anagram(first_string, second_string):
    if (
        first_string == ""
        or second_string == ""
        or len(first_string) != len(second_string)
    ):
        return False

    first_dict = create_dict_from_string(first_string)
    second_dict = create_dict_from_string(second_string)

    return first_dict == second_dict
