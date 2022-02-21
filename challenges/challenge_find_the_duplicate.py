from challenges.merge_sort import merge_sort
from challenges.binary_search import binary_search


def find_duplicate(nums):
    if type(nums) is not list or len(nums) < 2:
        return False

    ordenated_nums = merge_sort(nums)
    duplicate = False

    for index, number in enumerate(ordenated_nums):
        array_to_search = list(ordenated_nums)
        array_to_search.pop(index)

        if type(number) is not int or number < 1:
            break

        if binary_search(array_to_search, number):
            duplicate = number
            break

    return duplicate
