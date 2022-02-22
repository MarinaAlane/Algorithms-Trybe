nums = [-1, -1]
from collections import defaultdict


def find_duplicate(nums):
    dictionary = defaultdict(int)
    for i in nums:
        try:
            if i < 0:
                return False
            else:
                dictionary[i] += 1
                if dictionary[i] > 1:
                    return i
        except Exception as e:
            print(e)
            return False
    return False
