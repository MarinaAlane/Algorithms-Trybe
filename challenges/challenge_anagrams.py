def count_letter_string(str):
    string = {}
    for letter in str:
        if letter in string:
            string[letter] += 1
        else:
            string[letter] = 1
    return string


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    string1 = count_letter_string(first_string)
    string2 = count_letter_string(second_string)
    
    
    if not string1 and string2 or string1 != string2:
        return False
    else:
        for index in string1:
            if not index in string2:
                return False
            if not string1[index] == string2[index]:
                return False

        for index in string2:
            if not index in string1:
                return False
            if not string1[index] == string2[index]:
                return False

        return True
        
           