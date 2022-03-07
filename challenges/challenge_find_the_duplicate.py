def find_duplicate(nums):
    for num in nums:
        if type(num) != int or num < 1:
            return False
        
        if nums.count(num) > 1:
            return num
    return False
