def is_palindrome_recursive(word, low_index, high_index):
    # Palavra vazia retorna False
    if word == '':
        return False

    # Se as letras forem diferentes não é palíndromo.
    if word[low_index] != word[high_index]:
        return False

    # Se a palavra for um palíndromo par...
    # ... o low_index será maior que o high em algum momento.
    # Se for um palíndromo ímpar os índices serão iguais na letra do meio.
    if low_index >= high_index:
        return True

    # Para verificar as proximas letras, deve-se...
    # Adicionar +1 ao low_index e subtrair -1 do high_index.
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
