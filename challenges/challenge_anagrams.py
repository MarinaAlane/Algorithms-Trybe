from itertools import permutations


def selection_sort(word):
    return list(permutations(word))


print(selection_sort('carro'))


def is_anagram(first_string, second_string):
    string1 = selection_sort(first_string)
    string2 = selection_sort(second_string)

    if string1 == string2:
        return True
    else:
        return False
