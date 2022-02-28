def find_duplicate(nums):
    if len(nums) < 2 or type(nums) is not int:
        return False
    for i in range(len(nums)):
        if (i == i + 1):
            return i
