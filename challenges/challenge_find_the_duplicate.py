def find_duplicate(nums):
    if not nums or type(nums) is str:
        return False
    for i, number in enumerate(nums):
        if type(number) is str or number < 0:
            return False
        if number in nums[i + 1:]:
            return number
    return False
