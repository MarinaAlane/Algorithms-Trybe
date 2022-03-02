def find_duplicate(nums):
    if len(nums) <= 1:
        return False

    duplicated_number = False
    sorted_nums = nums
    sorted_nums.sort()
    for i, j in enumerate(sorted_nums):
        if isinstance(j, str) or j < 0:
            return False

        curr = j
        prev = sorted_nums[i - 1]

        if curr == prev:
            duplicated_number = curr

    return duplicated_number
