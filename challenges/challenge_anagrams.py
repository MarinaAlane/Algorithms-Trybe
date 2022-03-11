def is_anagram(first_string, second_string):
    if(first_string == '' or second_string == ''):
        return False
    if(len(first_string) != len(second_string)):
        return False
    return custom_sort(first_string) == custom_sort(second_string)


def custom_sort(string):
    new_string = list()
    string = list(string)
    while(string):
        min = string[0]
        for char in string:
            if(char <= min):
                min = char
        string.remove(min)
        new_string.append(min)
    return new_string
