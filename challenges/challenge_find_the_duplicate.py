def find_duplicate(nums):
    if len(nums) == 0:
        return False

    for num in nums:
        if type(num) != int:
            return False
        if num < 0:
            return False
        if nums.count(num) > 1:
            return num
    return False
