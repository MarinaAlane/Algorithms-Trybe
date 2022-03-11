def find_duplicate(nums):
    set_nums = set()
    for n in nums:
        if n in set_nums and n > 0:
            return n
        set_nums.add(n)
    return False
