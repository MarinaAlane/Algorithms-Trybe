def mySort(array):
    myList = list(array)

    for index in range(0, len(myList)):
        min_index = index

        for index_right in range(index + 1, len(myList)):
            if myList[index_right] < myList[min_index]:
                min_index = index_right

        myList[index], myList[min_index] = myList[min_index], myList[index]

    return myList


def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    else:
        first_list = mySort(list(first_string))
        second_list = mySort(list(second_string))

        position = 0

        while position < len(first_string) and True:
            if first_list[position] == second_list[position]:
                position = position + 1
            else:
                return False

        return True


if __name__ == '__main__':
    first_string = "amor"
    second_string = "roma"
    # saída: True
    # Explicação: Nesse caso o retorno da função é True,
    # pois a palavra "roma" é um anagrama de "amor".
    print(is_anagram(first_string, second_string))

    first_string = "pedra"
    second_string = "perda"
    # saída: True
    print(is_anagram(first_string, second_string))

    first_string = "pato"
    second_string = "tapo"
    # saída: True
    print(is_anagram(first_string, second_string))

    # Agora vamos pra um exemplo onde não existe um anagrama
    first_string = "coxinha"
    second_string = "empada"
    # saída: False
    print(is_anagram(first_string, second_string))

    # Agora vamos pra um exemplo onde uma das strings está em vazia
    first_string = ""
    second_string = "empada"
    # saída: False
    print(is_anagram(first_string, second_string))

    first_string = "coxinha"
    second_string = ""
    # saída: False
    print(is_anagram(first_string, second_string))
