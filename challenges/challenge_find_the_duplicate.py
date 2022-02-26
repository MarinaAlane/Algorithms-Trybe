def find_duplicate(nums):
    for i in range(len(nums)):
        if type(nums[i]) is str:
            return False
        if nums[i] < 0:
            return False
        if nums[i] in nums[i + 1 :]:
            return nums[i]
    return False
