def find_duplicate(nums):
    for num in nums:
        if isinstance(num, str) or num < 0:
            return False
        if len(nums) < 2:
            return False
        any_number_duplicate = nums.count(num)
        if any_number_duplicate > 1:
            return num
    return False


print(find_duplicate([1, 3, 4, 2, 2]))  # 2
print(find_duplicate([3, 1, 3, 4, 2]))  # 3
print(find_duplicate([1, 1]))  # 1
print(find_duplicate([1, 1, 2]))  # 1
print(find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8]))  # 7
print(find_duplicate([1]))  # False
print(find_duplicate([1, -5]))  # False
print(find_duplicate(['Brasil']))  # False
