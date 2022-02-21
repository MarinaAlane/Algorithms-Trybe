def order_letters(word):
    lista = list(word)
    swapped = True
    iterations = 0
    separator = ''

    while swapped:
        swapped = False

        for letter in range(len(lista) - iterations - 1):
            if lista[letter] > lista[letter + 1]:
                lista[letter], lista[letter + 1] = lista[letter + 1], lista[letter]

                swapped = True
        iterations += 1
    return separator.join(lista)


print(order_letters('bola'))