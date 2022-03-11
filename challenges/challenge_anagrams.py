def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    obj_1 = working_obj(first_string)
    obj_2 = working_obj(second_string)
    array_keys = list(obj_1.keys())
    return invert_word(array_keys, obj_1, obj_2)


# codigo extraido dos exercicios do course
# onde exercemos um algoritmo de força bruta
# conseguindo criar nossa proprio sort


def invert_word(phrase, obj_1, obj_2):
    for i in phrase:
        try:
            if obj_1[i] != obj_2[i]:
                return False
        except KeyError:
            return False
    return True


def working_obj(word):
    obj = {}
    reference = 0
    for letter in word:
        obj[letter] = 0
    array_keys = list(obj.keys())
    while reference < len(array_keys):
        for i in range(len(word)):
            if array_keys[reference] == word[i]:
                obj[word[i]] = obj[word[i]] + 1
        reference = reference + 1
    return obj
