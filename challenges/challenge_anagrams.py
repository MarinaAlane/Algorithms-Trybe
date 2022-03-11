def my_counter(string):
    first_counter = {}
    for letra in string:
        if letra in first_counter:
            first_counter[letra] += 1
        else:
            first_counter[letra] = 1
    return first_counter


def is_anagram(first_string, second_string):
    return my_counter(first_string) == my_counter(second_string)


def is_anagram_v2(first_string, second_string):
    # shortest case, if the strings dont have the same length
    # hello != helloo
    if len(first_string) != len(second_string):
        return False
    # common case
    for letra in first_string:
        """ if the second string contains the "letra"=lether of the first
        string it gets removed from the second string """
        second_string = second_string.replace(letra, '', 1)
    """ if all the lethers are removed, that means that both words have the
    same amount of equal lethers, therefore they are anagrams """
    return len(second_string) == 0
