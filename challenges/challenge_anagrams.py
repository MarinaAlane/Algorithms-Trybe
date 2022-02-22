def selection_sort(array):
    for i in range(len(array)):
        minimum = i

        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j

        array[minimum], array[i] = array[i], array[minimum]

    return array


def is_anagram(first_string, second_string):
    try:
        return selection_sort(
            list(first_string)
        ) == selection_sort(list(second_string))
    except ValueError:
        return False
