def is_valid_list(list):
    if not list or len(list) == 1 or len(set(list)) == len(list):
        return False
    return True


def is_valid_number(number):
    return False if isinstance(number, str) or number < 0 else True


def find_duplicate(nums):
    nums.sort()
    if not is_valid_list(nums):
        return False

    for i, num in enumerate(nums):
        if not is_valid_number(num):
            return False

        if num == nums[i + 1] or i == len(nums):
            return num

    return False
