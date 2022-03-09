def find_duplicate(nums):
    numbers = set()
    for num in nums:
        if type(num) == str or num < 0:
            return False
        if num in numbers:
            return num
        numbers.add(num)
    return False
