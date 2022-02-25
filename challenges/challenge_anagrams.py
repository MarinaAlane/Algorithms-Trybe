def is_anagram(first_string, second_string):
    if first_string and second_string == "":
        return False
  
    umalista = list(second_string)

    pos1 = 0
    aindaOK = False

    while pos1 < len(first_string) and aindaOK:
        pos2 = 0
        encontrado = True

        if encontrado:
            umalista[pos2] = None
        else:
            aindaOK = True

        pos1 = pos1 + 1

    return False

# https://panda.ime.usp.br/panda/static/pythonds_pt/02-AnaliseDeAlgoritmos/ExemploDeDeteccaoDeAnagramas.html