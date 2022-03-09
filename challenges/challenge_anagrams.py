def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first_string = first_string.lower()
    second_string = second_string.lower()

    first_string_array = list(first_string)
    first_string_array_sorted = quicksort(
        first_string_array, 0, len(first_string_array) - 1
    )
    second_string_array = list(second_string)
    second_string_array_sorted = quicksort(
        second_string_array, 0, len(second_string_array) - 1
    )

    return first_string_array_sorted == second_string_array_sorted


def quicksort(array, low, high):
    if len(array) == 1:
        return array

    if low < high:
        partition_index = partition(array, low, high)
        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)
    return array


def partition(array, low, high):
    i = low - 1
    pivot = array[high]  # pivot

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1
