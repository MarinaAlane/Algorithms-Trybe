def is_anagram(first_string, second_string):
    """ Faça o código aqui"""

    if len(first_string) != len(second_string):
        return False
    # criando dois hashmaps para contagem de palavras
    FS, SS = {}, {}

    for i in range(len(first_string)):  # iterando através de qualquer string
        # A função get ajudará a lidar com o erro de chave default 0
        FS[first_string[i]] = 1 + FS.get(first_string[i], 0)
        SS[second_string[i]] = 1 + SS.get(second_string[i], 0)

    for c in FS:
        # se ambas as strings não forem então retorna false
        if FS[c] != SS.get(c, 0):
            return False

    return True  # Sendo igual, retorn True
