def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    obj_1 = pop_obj(first_string)
    obj_2 = pop_obj(second_string)
    array_keys = list(obj_1.keys())
    return compare_strings(array_keys, obj_1, obj_2)


def compare_strings(array_keys, obj_1, obj_2):
    for i in array_keys:
        try:
            if obj_1[i] != obj_2[i]:
                return False
        except KeyError:
            return False
    return True


def pop_obj(word):
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
