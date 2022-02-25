def check_is_valid_array(nums):
    try:
        for num in nums:
            if num < 0:
                return False
    except TypeError:
        return False


def find_duplicate(nums):

    if len(nums) <= 1:
        return False

    if check_is_valid_array(nums) is False:
        return False

    sorted_nums = sorted(nums)

    if sorted_nums[0] == sorted_nums[1]:
        return sorted_nums[0]
    else:
        return find_duplicate(sorted_nums[1:])
