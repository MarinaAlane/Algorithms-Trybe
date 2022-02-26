# Função auxiliar construída baseada no link:
# https://www.programiz.com/python-programming/methods/dictionary/setdefault

def check_string(string):
    word = {}
    for letter in string:
        word[letter] = word.setdefault(letter, 0) + 1
        # percorre todo o laço e conta o total de letras da palavra
        # setdefault é um método do dicionário Python, com chave e valor
    # print('por aqui passa o laço for', word)
    return word


# percorreu todo o laço for e conta o número de letras
# print(check_string('Telefone'))
# {'T': 1, 'e': 3, 'l': 1, 'f': 1, 'o': 1, 'n': 1}


def is_anagram(first_string, second_string):
    string1 = check_string(first_string)
    string2 = check_string(second_string)
    if string1 == string2:
        return True
    else:
        return False


print(is_anagram('amor', 'roma'))  # True
print(is_anagram('coxinha', 'empada'))  # False
