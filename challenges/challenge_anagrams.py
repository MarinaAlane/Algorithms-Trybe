def is_anagram(first_string, second_string):
    try:
        first_word = quick_sort(split(first_string))
        second_word = quick_sort(split(second_string))
        return first_word == second_word

    except TypeError:
        return False


def split(word):
    chars = [item for item in word]
    return chars


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    higher_items = []
    lower_items = []

    for item in sequence:
        if item > pivot:
            higher_items.append(item)

        else:
            lower_items.append(item)

    return quick_sort(lower_items) + [pivot] + quick_sort(higher_items)
