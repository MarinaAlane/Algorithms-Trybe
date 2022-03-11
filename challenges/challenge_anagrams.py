def is_anagram(first_string, second_string):
    if(first_string == '' or second_string == ''):
        return False
    if(len(first_string) != len(second_string)):
        return False
    return custom_sort(first_string) == custom_sort(second_string)


def custom_sort(string):
    new_string = ""
    min = string[0]
    while(len(string) > 0):
        for char in string:
            if(char < min):
                min = char
        string.replace(min, None, 1)
        new_string += min
    return new_string
