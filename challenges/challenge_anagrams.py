#  https://app.betrybe.com/course/computer-science/algoritmos/algoritmos-de-ordenacao-e-busca/29521083-44ea-488d-a74d-216b1ac79b04/conteudos/60672880-f607-40d3-92fc-e551b740a91f/algoritmos-de-ordenacao/fd503999-673b-443d-afb1-ffcc5d1718f4?use_case=side_bar

# Ordenação por Seleção (Selection Sort)
def selection_sort(strings):
    # como um algoritmo de força bruta
    array = list(strings)
    # percorre a estrutura do array da lista exaustivamente
    for i in range(len(array)):
        minimum = i
    # itera sobre os elementos não ordenados
    for j in range(i + 1, len(array)):
        # seleciona o menor valor
        if array[j] < array[minimum]:
            minimum = j

     # após encontrar o menor valor
     # ao invés de criar um novo array
     # (o que aumenta complexidade de espaço)
     # realizamos a substituição entre o menor elemento
     # e a posição i que corresponde ao primeiro elemento não ordenado
     # que consequentemente passará a ser o último ordenado
    array[minimum], array[i] = array[i], array[minimum]

    return array


print(selection_sort('carro'))


def is_anagram(first_string, second_string):
    if selection_sort(first_string) == selection_sort(second_string):
        return True
    else:
        return False
