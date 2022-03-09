def find_duplicate(nums):
    nums_set = set(nums)
    for num in nums:
        if type(num) is str:
            return False
        elif num < 0:
            return False
        elif num in nums_set:
            nums_set.remove(num)
        else:
            return num
    return False
