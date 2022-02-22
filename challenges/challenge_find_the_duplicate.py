from challenges.utils.custom_numbers_sort import custom_numbers_sort


def validations(sorted_list):
    if not sorted_list:
        return False
    if sorted_list[0] == sorted_list[1]:
        return sorted_list[0]
    return find_duplicate(sorted_list[1:])


def find_duplicate(nums):
    try:
        if len(nums) <= 1:
            return False
        sorted_list = custom_numbers_sort(nums)
        return validations(sorted_list)
    except ValueError:
        return False
