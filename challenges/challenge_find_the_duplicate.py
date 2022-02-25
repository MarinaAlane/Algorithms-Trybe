def find_duplicate(nums):
    if len(nums) < 2:
        return False
    for item in nums:
        if isinstance(item, str) or item < 0:
            return False
