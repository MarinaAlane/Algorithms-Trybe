def find_duplicate(nums):
    """ Faça o código aqui. """
    try:
        numbers = set()
        for num in nums:
            if num in numbers:
                return num
            if num < 0:
                return False
            numbers.add(num)
    except TypeError:
        return False
    return False
