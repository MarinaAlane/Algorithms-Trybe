from collections import defaultdict


def find_iteration(nums):
    dictionary = defaultdict(int)
    for i in nums:
        if i < 0:
            return False
        else:
            dictionary[i] += 1
            if dictionary[i] > 1:
                return i
    return False


def find_duplicate(nums):
    try:
        return find_iteration(nums)
    except Exception:
        return False
