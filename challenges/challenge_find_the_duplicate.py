def find_duplicate(nums):
    for index, out_number in enumerate(nums):
        for in_number in nums[index + 1:]:
            if type(out_number) is str or out_number < 0:
                return False
            if out_number == in_number:
                return out_number
    return False
