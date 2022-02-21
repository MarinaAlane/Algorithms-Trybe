from challenges.merge_sort import merge_sort


def is_anagram(first_string, second_string):
    first_array = list(first_string)
    second_array = list(second_string)

    ordenated_first_array = merge_sort(first_array)
    ordenated_second_array = merge_sort(second_array)

    ordenated_first_string = "".join(ordenated_first_array)
    ordenated_second_string = "".join(ordenated_second_array)

    return ordenated_first_string == ordenated_second_string
