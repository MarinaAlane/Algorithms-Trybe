def find_duplicate(nums):
    """ Faça o código aqui. """
    nums.sort()
    duplicate = ''
    if len(nums) == 1:
        return False
    for index, number in enumerate(nums):
        if (type(number) is not int) or (number < 0):
            return False
        elif index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                duplicate = number
                break
            else:
                duplicate = False
    return duplicate
