def char_dict(string):
    string_dict = dict()

    for letter in string:
        try:
            string_dict[letter] += 1
        except KeyError:
            string_dict[letter] = 1
    
    return string_dict

def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False

    if len(first_string) != len(second_string):
        return False

    return char_dict(first_string) == char_dict(second_string)
