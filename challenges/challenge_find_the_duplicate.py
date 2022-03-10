from collections import defaultdict

def array_to_dict(array):
    my_dict = defaultdict(lambda: 0)
    for num in array:
        my_dict[num] += 1

    return my_dict


def find_duplicate(nums):
    if len(nums) == 0 :
        return False

    for number in nums:
        if type(number) is str:
            return False
        if number < 0:
            return False
    
    dict = array_to_dict(nums)
    if max(dict.values()) < 2:
        return False

    return max(dict, key=dict.get)