# reference https://stackoverflow.com/questions/14681096/
# typeerror-isinstance-arg-2-must-be-a-type-or-tuple-of-types
# reference https://realpython.com/python-enumerate/


def find_duplicate(nums):
    while len(nums) <= 1:
        return True

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
