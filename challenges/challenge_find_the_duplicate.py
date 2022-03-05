def find_duplicate(nums):
    if not nums:
        return False

    for number in nums:
        if isinstance(number, str) or number < 0:
            return False
        
        if nums.count(number) > 1:
            return number
        
    return False
