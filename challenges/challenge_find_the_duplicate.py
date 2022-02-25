def find_duplicate(nums):
    for index in nums:
        if (type(index) != int) or (len(nums) == 1) or (index < 0):
            return False

    nums.sort()

    for num in range(len(nums) - 1):
        if nums[num] == nums[num + 1]:
            return nums[num]
    return False


print(find_duplicate([1, 3, 4, 2, 2]))
