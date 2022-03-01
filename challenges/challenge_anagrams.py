#  helper function:
def string_counter(string):
    # ajudinha:
    # https://stackoverflow.com/questions/48217471/is-it-possible-to-check-for-anagram-without-using-sorted-or-dictionary-that-pe
    # O método setdefault() retorna o valor do item com a
    # chave especificada. Se a chave não existir, insira a chave,
    # com o valor especificado
    all_strings = {}
    for s in string:
        all_strings[s] = all_strings.setdefault(s, 0) + 1
    return all_strings


# requirement function:
def is_anagram(first_string, second_string):
    string1 = string_counter(first_string)
    string2 = string_counter(second_string)
    return string1 == string2
