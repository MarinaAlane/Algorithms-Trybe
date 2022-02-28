def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False

    if len(first_string) != len(second_string):
        return False

    first_string = first_string.lower()
    second_string = second_string.lower()

    for character in first_string:
        second_string = second_string.replace(character, '', 1)
    if len(second_string) == 0:
        return True
    return False

    # a função is_anagram recebe duas strings como parametro e verifica se as
    # duas sao anagramas uma da outra.
    # o primeiro teste é feito a fim de identificar se as duas strings contem
    # algo. Se não, retorna false.
    # posteriormente identifica-se o tamanho de cada uma das strings, se o
    # tamanho for diferente retorna-se falso, já que para ser anagrama é
    # necessário ter a mesma quantidade de letras.
    # transforma-se então as letras das duas strings em minusculas, ja que há
    # diferença entre maiusculas e minusculas.
    # faço entao um for em first_string que pega cada letra da frase e
    # substitui por um '' na second_string. Se no final do for o tamanho do
    # second_string for igual a zero, significa que as duas strings são
    # anagramas. Se restar algo em second string, entao nao é anagrama.
    # https://www.programiz.com/python-programming/methods/string/replace
