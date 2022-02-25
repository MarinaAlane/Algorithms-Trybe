def find_duplicate(nums):
    """ Faça o código aqui. """
    for first_num in range(0, len(nums)):
        for second_num in range(1, len(nums)):
            if nums[first_num] == nums[second_num] and first_num != second_num:
                print(f"sozinho {first_num}")
                print(f"sozinho {second_num}")
                return nums[first_num]


print(find_duplicate([1, 2, 3, 4, 2]))
