def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    if word[low_index] == word[high_index]:
        if low_index >= high_index:
            return True
        low_index += 1
        high_index -= 1
        is_palindrome_recursive(word, low_index, high_index)
    return False

# is_palindrome_recursive é uma função que recebe como parametros uma palavra,
# o index da primeira letra(low_index) e o index da ultima letra(high_index).
# priemrio verifico se a word esta vazia ou nao, se sim retorna falso. Depois
# verifico se a letra no indice low_index é igual a letra da palavra no indice
# high_index. Se sim qcrescento um a low index e decremento um em high index.
# chamo entao por recursividade a função passando a mesma palavra, mas agora
# com os indices atualizados para verificar as letras subsequentes(tanto
# crescentemente, quanto decrescentemente)


# Uma alternativa de resolução é:
# for i in range(high_index // 2):
#     if word[low_index] != word[high_index]:
#         return False
#     low_index += 1
#     high_index -= 1
#     is_palindrome_recursive(word, low_index, high_index)
#     if word[low_index] != word[high_index]:
#         return False
# return True
