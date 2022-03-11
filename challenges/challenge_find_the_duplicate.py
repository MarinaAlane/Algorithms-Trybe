def find_duplicate(nums):
    numbers = list()

    for number in nums:
        if not isinstance(number, int) or number < 0:
            return False
        if number in numbers:
            return number
        numbers.append(number)
    return False
