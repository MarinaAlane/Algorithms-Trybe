def find_duplicate(nums):
    """ Faça o código aqui. """
    numbers = list()


# https://www.w3schools.com/python/ref_func_isinstance.asp

    for number in nums:
        if isinstance(number, str) or number < 0:
            return False

        if number in numbers:
            return number
            numbers.add(number)

    return False
