def quicksort(string):
    if not string:
        return string

    pivot = string[0]

    head = quicksort([x for x in string[1:] if x < pivot])
    tail = quicksort([x for x in string[1:] if x > pivot])

    return head + [x for x in string if x == pivot] + tail


def is_anagram(first_string, second_string):
    return quicksort(first_string) == quicksort(second_string)
