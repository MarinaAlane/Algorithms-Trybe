def sort(word):
    array = list(word)
    array_sorted = []

    while array:
        small = min(array)
        array_sorted.append(small)
        array.pop(array.index(small))

    return "".join(array)
