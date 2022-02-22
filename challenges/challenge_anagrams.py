def character_count(string):
    string_dict = {}
    for char in string:
        if char in string_dict:
            string_dict[char] += 1
        else:
            string_dict[char] = 0
    return string_dict
    

def is_anagram(first_string, second_string):
    first_string_dict = character_count(first_string)
    second_string_dict = character_count(second_string)
    if len(first_string_dict) != len(second_string_dict):
        return False
    for key in first_string_dict:
        if key not in second_string_dict:
            return False
        if first_string_dict[key] != second_string_dict[key]:
            return False
    return True
  