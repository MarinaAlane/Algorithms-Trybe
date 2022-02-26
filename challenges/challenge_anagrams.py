# https://www.youtube.com/watch?v=UBg3nJrGOKg
# https://pt.stackoverflow.com/questions/506774/ordena%C3%A7%C3%A3o-com-selection-sort-por-tamanho-e-alfabeticamente
def sort_list(lista):
    i = 1
    for i in range(len(lista)):
        temp = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > temp:
            lista[j + 1] = lista[j]
            j -= 1
            lista[j + 1] = temp
        i += 1
    return lista


def is_anagram(first_string, second_string):
    if (
        first_string == ""
        or second_string == ""
        or len(first_string) != len(second_string)
    ):
        return False
    if sort_list(list(first_string)) == sort_list(list(second_string)):
        return True
    return False
