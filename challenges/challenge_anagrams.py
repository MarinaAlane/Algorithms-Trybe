def is_anagram(first_string, second_string):
    try:
        first_result = quick_sort(split(first_string))
        second_result = quick_sort(split(second_string))
        return first_result == second_result

    except TypeError:
        return False


def split(word):
    chars = [item for item in word]
    return chars


# https://www.youtube.com/watch?v=kFeXwkgnQ9U
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
