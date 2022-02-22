# https://panda.ime.usp.br/panda/static/pythonds_pt/02-AnaliseDeAlgoritmos/ExemploDeDeteccaoDeAnagramas.html
def solucaoAnagrama(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    aindaOK = True
    while j<26 and aindaOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            aindaOK = False

    return aindaOK

def is_anagram(first_string, second_string):
    if(solucaoAnagrama(first_string, second_string)):
        return True
    else:
        return False


