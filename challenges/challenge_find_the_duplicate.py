def find_duplicate(nums):
    if len(nums) < 2:
        return False

    for item in nums:
        if isinstance(item, str) or item < 0:
            return False

    nums.sort()

    if not len(set(nums)) == len(nums):
        for number1 in list(set(nums)):
            count = 0
            for number2 in nums:
                if number1 == number2:
                    count += 1
                    if count > 1:
                        return number1
    return False
