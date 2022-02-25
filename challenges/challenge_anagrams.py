def counter_letters(term):
    counter = dict()

    # Ajuda do Issac no plantão de CS
    # https://www.w3schools.com/python/ref_dictionary_get.asp

    # Se a letra não existir, criará uma chave com a letra com o valor 1.
    # Se ela já existir adicionará +1 no valor.

    for i in term:
        counter[i] = counter.get(i, 0) + 1

    return counter


def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False

    if len(first_string) != len(second_string):
        return False

    first_string_quantity = counter_letters(first_string)
    second_string_quantity = counter_letters(second_string)

    return first_string_quantity == second_string_quantity


print(is_anagram('pedrra', 'perrda'))
