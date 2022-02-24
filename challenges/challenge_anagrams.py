def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    word_one = merge_sort(list(first_string))
    word_two = merge_sort(list(second_string))

    return word_one == word_two


# Based on src:
# https://www.educative.io/edpresso/merge-sort-in-python
def merge_sort(word):
    if (len(word) < 2):
        return word

    mid = len(word)//2
    left, right = merge_sort(word[:mid]), merge_sort(word[mid:])
    return merge(left, right, word.copy())


def merge(left, right, merged):
    i = 0
    j = 0

    main = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged[main] = left[i]
            i += 1
        else:
            merged[main] = right[j]
            j += 1
        main += 1

    while i < len(left):
        merged[main] = left[i]
        i += 1
        main += 1

    while j < len(right):
        merged[main] = right[j]
        j += 1
        main += 1

    return merged
