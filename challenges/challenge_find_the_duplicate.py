def find_duplicate(nums):
    for n in nums:
        if not isinstance(n, int) or n < 1:
            return False

        if nums.count(n) > 1:
            return n

    return False
