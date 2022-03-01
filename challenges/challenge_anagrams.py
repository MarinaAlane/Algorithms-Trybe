def quicksort(lista, esquerda=0, direita=None):
    if direita is None:
        direita = len(lista)-1
    if esquerda < direita:
        pivot = partition(lista, esquerda, direita)
        quicksort(lista, esquerda, pivot - 1)
        quicksort(lista, pivot + 1, direita)

    return lista


def partition(lista, esquerda, direita):
    pivot = lista[direita]
    i = esquerda
    for j in range(esquerda, direita):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i], lista[direita] = lista[direita], lista[i]
    return i


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if (len(first_string) != len(second_string)
            or first_string == '' or second_string == ''):
        return False

    primeira = quicksort(list(first_string))
    segunda = quicksort(list(second_string))

    if primeira == segunda:
        return True
    return False
