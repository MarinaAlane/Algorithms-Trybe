def validate_nums(nums):
    if len(nums) < 2:
        return False

    for item in nums:
        if isinstance(item, str) or item < 0:
            return False

    return True


def find_duplicate(nums):
    if not validate_nums(nums):
        return False

    nums.sort()

    if not len(set(nums)) == len(nums):
        for index in range(len(nums)):
            if nums[index] == nums[index + 1]:
                return nums[index]

    return False
