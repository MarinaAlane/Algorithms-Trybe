def is_palindrome_recursive(word, low_index, high_index):
    """ Dado uma string, determine se ela é um palíndromo ou não. Escreva uma função que irá determinar se uma string é um palíndromo ou não. Um palíndromo é uma string, uma palavra, em que não faz diferença se ela é lida da esquerda para a direita ou vice-versa, pois ela mantêm o mesmo sentido. Por exemplo, "ABCBA". """
    if low_index == high_index:
        return True
    elif word[low_index] != word[high_index]:
        return False
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
