def separeChar(fs, ss):
    fObj = dict()
    sObj = dict()
    for index in range(len(fs)):
        if fs[index] in fObj:
            fObj[fs[index]] += 1
        else:
            fObj[fs[index]] = 1
        if ss[index] in sObj:
            sObj[ss[index]] += 1
        else:
            sObj[ss[index]] = 1
    all = dict()
    all['fObj'] = fObj
    all['sObj'] = sObj
    return all


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    res = separeChar(first_string, second_string)
    firstObj = res['fObj']
    secondObj = res['sObj']
    for index in range(len(first_string)):
        if first_string[index] not in secondObj:
            return False
        if firstObj[first_string[index]] != secondObj[first_string[index]]:
            return False
    return True
