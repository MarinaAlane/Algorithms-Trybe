def find_duplicate(nums):
    if len(nums) == 0 or len(nums) == 1:
        return False

    if any(isinstance(number, str) for number in nums):
        return False

    if any(number < 0 for number in nums):
        return False

    duplicated_number = False
    sorted_nums = nums
    sorted_nums.sort()
    for i, j in enumerate(sorted_nums):
        curr = j
        prev = sorted_nums[i - 1]
        if (
            duplicated_number is not False
            and curr == prev
            and duplicated_number != curr
        ):
            return False
        if curr == prev:
            duplicated_number = curr

    return duplicated_number
