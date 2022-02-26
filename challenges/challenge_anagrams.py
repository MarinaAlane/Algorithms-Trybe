def mySort(array):
    list_Object = list(array)

    for index in range(0, len(list_Object)):
        min_index = index
        for index_right in range(index + 1, len(list_Object)):
            if list_Object[index_right] < list_Object[min_index]:
                min_index = index_right
        list_Object[index], list_Object[min_index] = list_Object[min_index], list_Object[index]

    return list_Object


def is_anagram(first_string, second_string):
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
