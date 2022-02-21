# Teste de solução 1: Não passou na questão do tempo
# def order_letters(word):
#     lista = list(word)
#     swapped = True
#     iterations = 0
#     separator = ""

#     while swapped:
#         swapped = False

#         for letter in range(len(lista) - iterations - 1):
#             if lista[letter] > lista[letter + 1]:
#                 lista[letter], lista[letter + 1] = (
#                     lista[letter + 1],
#                     lista[letter],
#                 )

#                 swapped = True
#         iterations += 1
#     return separator.join(lista)


# def is_anagram(first_string, second_string):
#     return order_letters(first_string) == order_letters(second_string)

# Teste de solução 2: passou na questão do tempo

def merge_sort(word):
    array = list(word)
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, right, array.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):

        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def is_anagram(first_string, second_string):
    return merge_sort(first_string) == merge_sort(second_string)
