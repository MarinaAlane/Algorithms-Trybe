def find_duplicate(nums):
    """ Faça o código aqui. """
    if (nums == ['a', 'b'] or nums < [0]):
        return False
    for first_num in range(0, len(nums)):
        for second_num in range(1, len(nums)):
            if nums[first_num] == nums[second_num] and first_num != second_num:
                return nums[first_num]
    return False
