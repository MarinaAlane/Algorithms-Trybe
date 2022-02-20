def find_duplicate(nums):
    duplicate = False
    try:
        nums.sort()
        index = 0
        while not duplicate and index < len(nums) - 1:
            if nums[index] <= 0:
                break
            elif nums[index] == nums[index + 1]:
                duplicate = nums[index]
            else:
                index += 1
        return duplicate
    except Exception:
        return duplicate
