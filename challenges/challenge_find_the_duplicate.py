def find_duplicate(nums):
    if not nums or type(nums) is str:
        return False

    for index, num in enumerate(nums):
        if type(num) is str or num < 0:
            return False

        if num in nums[index + 1:]:
            return num

    return False
