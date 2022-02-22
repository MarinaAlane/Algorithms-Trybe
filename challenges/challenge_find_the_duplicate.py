def check_param(param):
    if not param or len(param) <= 1:
        return False
    else:
        for number in param:
            if not isinstance(number, int) or number < 0:
                return False
            else:
                return True


def find_duplicate(nums):
    """Faça o código aqui."""
    if not check_param(nums):
        return False
    for number in nums:
        if nums.count(number) > 1:
            return number
        else:
            continue
    return False
