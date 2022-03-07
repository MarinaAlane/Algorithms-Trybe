def mount_dict(nums):
    dictio = dict()
    for num in nums:
        if type(num) is not int or num < 0:
            return False
        try:
            dictio[num] += 1
        except KeyError:
            dictio[num] = 1

    return dictio


def find_duplicate(nums):
    dict_nums = mount_dict(nums)

    if not dict_nums:
        return False

    for key, value in dict_nums.items():
        if value > 1:
            return key

    return False
