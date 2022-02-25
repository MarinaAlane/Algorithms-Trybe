def find_duplicate(nums):
    if len(nums) <= 1:
        return False
    if validations(nums):
        return False

    nums.sort()
    for index in range(len(nums)):
        if nums[index] == nums[index + 1]:
            return nums[index]


def validations(list):
    if len(list) <= 2 and list[0] != list[1]:
        return True

    for element in list:
        if type(element) == str:
            return True
        if element < 1:
            return True
