from random import randint


def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item > pivot:
            high.append(item)
        else:
            same.append(item)

    return quicksort(low) + same + quicksort(high)


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first = quicksort(list(first_string).copy())
    second = quicksort(list(second_string).copy())

    if first == second:
        return True
    else:
        return False
