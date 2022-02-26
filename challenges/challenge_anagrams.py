def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    firstStringList = list(first_string)
    secondStringList = list(second_string)
    for letra in firstStringList:
        if secondStringList.__contains__(letra):
            secondStringList.remove(letra)
            if len(secondStringList) == 0:
                return True
        else:
            return False

    return True
