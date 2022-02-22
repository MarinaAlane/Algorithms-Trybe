# código do merge_sort do course
def merge_sort(array):
    if len(array) <= 1:
        return array
    # divide pela metade
    mid_array = len(array) // 2

    left_array, rigth_array = merge_sort(array[:mid_array]), merge_sort(
        array[mid_array:]
    )
    return merge(left_array, rigth_array, array[:])


# função auxiliar - mistura dos arrays (codigo do course)
def merge(left_array, rigth_array, merged):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left_array) and right_cursor < len(rigth_array):
        if left_array[left_cursor] <= rigth_array[right_cursor]:
            merged[left_cursor + right_cursor] = left_array[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = rigth_array[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left_array)):
        merged[left_cursor + right_cursor] = left_array[left_cursor]

    for right_cursor in range(right_cursor, len(rigth_array)):
        merged[left_cursor + right_cursor] = rigth_array[right_cursor]

    return merged


def is_anagram(first_string, second_string):
    # junta as palavras que vem na lista
    first_word = "".join(merge_sort(list(first_string)))
    second_word = "".join(merge_sort(list(second_string)))
    if not first_word or not second_word or first_word != second_word:
        return False
    return True


if __name__ == "__main__":
    print(is_anagram("amor", "roma"))
    print(is_anagram("pedra", "perda"))
    print(is_anagram("coxinha", "empada"))

# usando Merge sort => de acordo course: técnica da divisão e conquista.
# https://app.betrybe.com/course/computer-science/algoritmos/algoritmos-de-ordenacao-e-busca/29521083-44ea-488d-a74d-216b1ac79b04/conteudos/60672880-f607-40d3-92fc-e551b740a91f/algoritmos-de-ordenacao/fd503999-673b-443d-afb1-ffcc5d1718f4?use_case=side_bar
# Video sobre merge sort: https://www.youtube.com/watch?v=5prE6Mz8Vh0
# https://stackoverflow.com/questions/2597119/sorting-elements-in-string-with-python
# https://www.geeksforgeeks.org/python-string-join-method/
