def find_duplicate(nums):
    separator = ''
    result = False
    lista = sorted(nums)
    print(lista)
    if len(nums) < 2:
        return False
    elif '-' in separator.join(str(nums) for e in nums):
        return False
    if lista[0] == lista[1]:
        result = lista[0]
    return result


print(find_duplicate([1, 2, 3, 2, 4]))