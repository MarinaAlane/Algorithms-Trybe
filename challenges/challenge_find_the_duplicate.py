def find_duplicate(nums):
    """ Faça o código aqui. """
    nums.sort()
    duplicate = ''
    for index, num in enumerate(nums):
        if (type(num) is not int) or (num < 0) or (index == len(nums) - 1):
            return False
        elif nums[index] == nums[index + 1]:
            duplicate = num
            break
        else:
            duplicate = False
    return duplicate
