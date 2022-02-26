def counts_words(string):
    list = dict()
    for item in string:
        list[item] = list.setdefault(item, 0) + 1
        # https://www.w3schools.com/python/ref_dictionary_setdefault.asp

    return list


def is_anagram(string1, string2):
    str1 = counts_words(string1)
    str2 = counts_words(string2)

    if (str1 == str2):
        return True
    else:
        return False
