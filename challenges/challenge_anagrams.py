def my_sort(array):
    for i in range(len(array)):
        current_value = array[i]
        current_index = i

        while (
            current_index > 0
            and array[current_index - 1] > current_value
        ):

            array[current_index] = array[current_index - 1]
            current_index = current_index - 1

        array[current_index] = current_value
    return array


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    first_list = list(first_string)
    second_list = list(second_string)

    if len(first_list) != len(second_list):
        return False

    if my_sort(first_list) == my_sort(second_list):
        return True
    else:
        return False