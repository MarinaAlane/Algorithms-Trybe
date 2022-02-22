def aux(first_string, second_string):
    first_string = list(first_string)
    second_string = list(second_string)
    copy = ''
    for item in first_string:
        for index in range(0, len(second_string)):
            if second_string[index] == item:
                copy = copy + second_string[index]
                second_string.pop(index)
                break
    return second_string

def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) == len(second_string) == 0:
        return False    
    if len(first_string) != len(second_string):
        return False
    # first_string = list(first_string)
    # second_string = list(second_string)
    # copy = ''
    # for item in first_string:
    #     for index in range(0, len(second_string)):
    #         if second_string[index] == item:
    #             copy = copy + second_string[index]
    #             second_string.pop(index)
    #             break

    if len(aux(first_string, second_string)) == 0:
        return True
    return False

# print(is_anagram('pedrra', 'pedraa'))
# print(is_anagram('pedraa', 'pedrra'))
