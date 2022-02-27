def createCharacterSeparate(first_string, second_string):
    obj1 = dict()
    obj2 = dict()

    for index in range(len(first_string)):
        if first_string[index] in obj1:
            obj1[first_string[index]] += 1
        else:
            obj1[first_string[index]] = 1
        if second_string[index] in obj2:
            obj2[second_string[index]] += 1
        else:
            obj2[second_string[index]] = 1

    allObj = dict()
    allObj["obj1"] = obj1
    allObj["obj2"] = obj2

    return allObj


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) != len(second_string):
        return False

    response = createCharacterSeparate(first_string, second_string)
    obj1 = response["obj1"]
    obj2 = response["obj2"]

    for index in range(len(first_string)):
        if first_string[index] not in obj2:
            return False
        if obj1[first_string[index]] != obj2[first_string[index]]:
            return False

    return True
