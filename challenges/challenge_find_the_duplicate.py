import string


def find_duplicate(nums):
    if (not nums or type(nums) == string or len(nums) == 1):
        return False

    return check_nums(nums)


def check_nums(nums):
    numb = sorted(nums)
    for i in range(1, len(numb)):
        if type(numb[i]) != int:
            return False
        if numb[i - 1] == numb[i]:
            return numb[i]
    return False
