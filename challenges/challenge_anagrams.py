def is_anagram(first_string, second_string):
    if "" in [first_string, second_string] or len(first_string) != len(
        second_string
    ):
        return False

    first_string = list(first_string)
    second_string = list(second_string)

    quicksort(first_string, 0, len(first_string) - 1)
    quicksort(second_string, 0, len(second_string) - 1)

    return first_string == second_string


def quicksort(array, low, high):
    if len(array) == 1:
        return array

    if low < high:
        partition_index = partition(array, low, high)

        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)


def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1
