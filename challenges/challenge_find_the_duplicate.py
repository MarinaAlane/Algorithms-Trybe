def find_duplicate(nums):
    result = [0, 0]
    for number in nums:
        if  type(number) == str or number < 0:
            return False
        if nums.count(number) > result[1]:
         result[0] = number
         result[1] = nums.count(number)
    if result[1] == 1:
        return False
    return result[0]

# array = [ 1, 2 ,1]
# print(array.count(2))
numero = "ae"
print(type(numero) is str)