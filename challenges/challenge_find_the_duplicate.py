def find_duplicate(nums):
    if len(nums) < 2:
        return False

    for index, num in enumerate(nums):
        if (not isinstance(num, int) or num < 0):
            return False

        if (nums[index] in nums[index + 1:]):
            return nums[index]

    return False
