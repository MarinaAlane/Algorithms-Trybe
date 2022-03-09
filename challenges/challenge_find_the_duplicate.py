def find_duplicate(nums):
    nums_set = set(nums)
    for num in nums:
        if type(num) is str:
            return False
        if num < 0:
            return False
        if num in nums_set:
            nums_set.remove(num)
        else:
            return num
    return False
