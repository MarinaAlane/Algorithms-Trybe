from tokenize import Number


def find_duplicate(nums):
    list = []
    for n in nums:
        if(type(n) != int or n < 0):
            return False
        if n in list:
            return n
        list.append(n)
    return False
