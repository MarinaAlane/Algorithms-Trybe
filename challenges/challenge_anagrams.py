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
    if first_string or second_string == '':
        result = False

    first_list = mySort(list(first_string))
    second_list = mySort(list(second_string))

    position = 0
    result = True

    while position < len(first_string) and result:
        if first_list[position] == second_list[position]:
            position = position + 1
        else:
            result = False

    return result
