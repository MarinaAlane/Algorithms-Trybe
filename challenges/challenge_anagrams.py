# from challenges.helper.merge_sort import merge_sort
from challenges.helper.quick_sort import quicksort


# def is_anagram(first_string, second_string):
#     first_string = merge_sort(list(first_string))
#     second_string = merge_sort(list(second_string))
#     return first_string == second_string

# src
# https://pythonguides.com/sorting-algorithms-in-python/

def is_anagram(first_string, second_string):
    first_array = list(first_string)
    second_array = list(second_string)
    quicksort(first_array, 0, len(first_array) - 1)
    quicksort(second_array, 0, len(second_array) - 1)
    return first_array == second_array
