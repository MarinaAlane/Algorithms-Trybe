def quick_sort(sequence):
    if len(sequence) <= 1:
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


def split(word):
    return [char for char in word]


def is_anagram(first_string, second_string):
    if quick_sort(split(first_string)) == quick_sort(split(second_string)):
        return True
    else:
        return False
