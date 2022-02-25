def validate_nums(nums):
    if (type(nums) != int) or (nums == '') or (len(nums) == 1) or (nums < 0):
        return False


def find_duplicate(nums):
    if not validate_nums(nums):
        return False

    nums.sort()

    if len(set(nums)) != len(nums):
        for num in range(len(nums)):
            if nums[num] == nums[num + 1]:
                return nums[num]

    return False
