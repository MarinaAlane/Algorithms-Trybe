def find_duplicate(nums):
    numbers_list = list()

    for n in nums:
        if not isinstance(n, int) or n < 0:
            return False
        if n in numbers_list:
            return n
        numbers_list.append(n)

    return False
