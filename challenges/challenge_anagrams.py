def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    array_first_string = selection_sort(first_string)
    array_second_string = selection_sort(second_string)
    for i in range(len(array_first_string)):
        if array_first_string[i] == array_second_string[i]:
            return True
        else:
            return False


# https://app.betrybe.com/course/computer-science/algoritmos/
#   algoritmos-de-ordenacao-e-busca/
#   29521083-44ea-488d-a74d-216b1ac79b04/conteudos/
#   60672880-f607-40d3-92fc-e551b740a91f/algoritmos-de-ordenacao/
#   fd503999-673b-443d-afb1-ffcc5d1718f4?use_case=side_bar
#   codigo de ordenação do curso da Trybe com a adição do
#   append para separa as letras
def selection_sort(word):
    # como um algoritmo de força bruta
    # percorre a estrutura exaustivamente
    word_array = []
    for letter in word:
        word_array.append(letter)
    for i in range(len(word_array)):
        minimum = i
        # itera sobre os elementos não ordenados
        for j in range(i + 1, len(word_array)):
            # seleciona o menor valor
            if word_array[j] < word_array[minimum]:
                minimum = j
        # após encontrar o menor valor
        # ao invés de criar um novo array
        # (o que aumenta complexidade de espaço)
        # realizamos a substituição entre o menor elemento
        # e a posição i que corresponde ao primeiro elemento não ordenado
        # que consequentemente passará a ser o último ordenado
        word_array[minimum], word_array[i] = word_array[i], word_array[minimum]

    return word_array
