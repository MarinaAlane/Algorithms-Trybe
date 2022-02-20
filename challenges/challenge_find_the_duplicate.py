def find_duplicate(nums):
    if len(nums) == 0:
        return False
    for element in nums:
        if not isinstance(element, int):
            return False
        if element < 0:
            return False
        if nums.count(element) > 1:
            return element
    return False
