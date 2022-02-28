def find_duplicate(nums):
    if len(nums) == 0:
        return False
    for num in nums:
        if not isinstance(num, int) or num < 1:
            return False
        if nums.count(num) > 1:
            return num
    return False

# https://thispointer.com/python-3-ways-to-check-if-there-are-duplicates-in-a-list/
