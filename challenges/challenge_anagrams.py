from challenges import sorting_algs


def is_anagram(first_string, second_string):
    if "" in [first_string, second_string] or len(first_string) != len(
        second_string
    ):
        return False

    first_string = list(first_string)
    second_string = list(second_string)

    sorting_algs.quicksort(first_string, 0, len(first_string) - 1)
    sorting_algs.quicksort(second_string, 0, len(second_string) - 1)

    return first_string == second_string
