def find_duplicate(nums):
    if not nums:
        return False
    if len(nums) == 1:
        return False
    for i in range(len(nums)):
        if type(nums[i]) is str:
            return False
        if nums[i] < 0:
            return False
        if nums[i] in nums[i + 1 :]:
            return nums[i]
    return False


nums = [1, 3, 4, 2, 2]

print(find_duplicate(nums))
