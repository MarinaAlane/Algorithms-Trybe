def is_anagram(first_string, second_string):
    """ Faça o código aqui"""

    while first_string != '':
        if len(first_string) != len(second_string):
            return False
        tmp = first_string[0]
        first_string = first_string.replace(tmp, '')
        try:
            second_string = second_string.replace(tmp, '')
        except:
            return False

    if second_string != '':
        return False
    else:
        return True