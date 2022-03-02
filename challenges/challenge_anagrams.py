def selection_sort(word):
    letters = [*word]
    for i in range(len(letters)):
        lowest_letter = i

        for j in range(i + 1, len(letters)):
            if letters[j] < letters[lowest_letter]:
                lowest_letter = j

        letters[lowest_letter], letters[i] = letters[i], letters[lowest_letter]

    return "".join(letters)


# implementação inspirada no selection sort do gabarito abaixo:
# https://app.betrybe.com/course/computer-science/algoritmos/algoritmos-de-ordenacao-e-busca-gabarito/solutions/b471328b-a7ef-4c62-ac38-743f15b38fad/gabarito-dos-exercicios/b9ef5713-3678-4570-890c-4b4de0b7cffa?use_case=calendar
# essa implementação funciona para comparação de caracteres pois a linguagem
# compara os valores da tabela ascii um potencial bug para a aplicação da forma
# que está implementada é não lidar com a capitalização de palavras como há
# limite de tempo um bypass para manter a capitalização das letras não foi
# implementado para preservar a performance.


def is_anagram(first_string, second_string):
    if first_string is None or second_string is None:
        return False

    first_string_sorted = selection_sort(first_string)
    second_string_sorted = selection_sort(second_string)
    return first_string_sorted == second_string_sorted
