def find_duplicate(nums):
    low = 0
    high = len(nums) - 1

    dic = dict()

    while low < high:
        if nums[low] in dic:
            return nums[low]
        elif nums[high] in dic:
            return nums[high]
        else:
            nums[high] = 1
            nums[low] = 1
        high -= 1
        low += 1

    return False
