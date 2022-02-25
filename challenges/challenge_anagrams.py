def sort_string(word):
    array = list(word)
    array_sorted = []

    while array:
        order = min(array)
        array_sorted.append(order)
        array.pop(array.index(order))

    return "".join(array_sorted)


def is_anagram(first_string, second_string):

    if sort_string(first_string) == sort_string(second_string):
        return True

    if not first_string or not second_string:
        return False

    if len(first_string) != len(second_string):
        return False

    return False
