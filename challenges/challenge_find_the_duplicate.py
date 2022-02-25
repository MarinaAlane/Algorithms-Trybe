def find_duplicate(nums):
    differente_number = []
    if len(nums) < 2:
        return False

    for item in nums:
        if isinstance(item, str) or item < 0:
            return False

    nums.sort()
    converted_list_to_set = set(nums)
    converted_set_to_list = list(converted_list_to_set)  # nums = [1, 2, 3, 4]

    if not len(converted_set_to_list) == len(nums):
        for numb1 in converted_set_to_list:
            count = 0
            for numb2 in nums:
                if numb1 == numb2:
                    count += 1
                    if count > 1:
                        return numb1
    return False
