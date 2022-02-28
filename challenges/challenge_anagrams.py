def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if fim - inicio > 1:
        meio = (fim + inicio) // 2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

    return lista


def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    first_string_chars = [char for char in first_string]
    second_string_chars = [char for char in second_string]

    if mergesort(first_string_chars) == mergesort(second_string_chars):
        return True
    else:
        return False


# https://www.devmedia.com.br/algoritmos-de-ordenacao-analise-e-comparacao/28261

# https://www.youtube.com/watch?v=5prE6Mz8Vh0
