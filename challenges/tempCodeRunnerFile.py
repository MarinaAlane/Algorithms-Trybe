def find_duplicate(nums):
    separator = ''
    result = ''
    lista = sorted(nums)
    if len(nums) < 2:
        return False
    elif '-' in separator.join(str(nums) for e in nums):
        return False
    for index, number in enumerate(lista):
        if lista[index] == lista[index - 1]:
            result = number
    return result
