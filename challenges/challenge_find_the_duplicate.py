def find_duplicate(nums):
    list = {}
    for num in nums:
        if num in list:
            list[num] += 1
        else:
            list[num] = 1
        if list[num] > 1:
            if num < 0:
                return False
            return num
    return False
