# https://www.techiedelight.com/find-duplicate-items-python-list/

def find_duplicate(nums):
    for elem in nums:
        if type(elem) != int or elem < 1:
            return False
        if nums.count(elem) > 1:
            dup = [x for i, x in enumerate(nums) if i != nums.index(x)]
            return dup[0]
    return False


find_duplicate([1, 2, 3, 4, 5, 5])
