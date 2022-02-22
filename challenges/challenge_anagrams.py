# https://panda.ime.usp.br/panda/static/pythonds_pt/02-AnaliseDeAlgoritmos/ExemploDeDeteccaoDeAnagramas.html
def solucaoAnagrama(s1, s2):
    pos = 0
    c1 = [pos]*26
    c2 = [pos]*26
    for i in range(len(s1)):
    # contar o número de vezes que cada caractere ocorre
        # ord recebe uma letra e retorna o código ASCII da mesma
        pos = ord(s1[i])-ord('a')
        # Cada vez que encontramos um caractere em particular,
        # incrementamos o seu contador naquela posição
        c1[pos] = c1[pos] + 1
        
    for i in range(len(s2)):
        # ord recebe uma letra e retorna o código ASCII da mesma
        pos = ord(s2[i])-ord('a')
        # Cada vez que encontramos um caractere em particular,
        # incrementamos o seu contador naquela posição
        c2[pos] = c2[pos] + 1

    j = 0
    anagram = True
    while j < 26 and anagram:
        # se as duas listas de contadores são idênticas, as strings são anagramas
        if c1[j] == c2[j]:
            j += 1
            return anagram
        else:
            anagram = False

    return anagram


def is_anagram(first_string, second_string):
    return (solucaoAnagrama(first_string, second_string))
