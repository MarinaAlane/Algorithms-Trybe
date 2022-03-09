def find_duplicate(nums):
    sset = set()
    if len(nums) < 2:
        return False
    for e in nums:
        if type(e) is not int or e < 0:
            return False
        sset.add(e)
    return False
