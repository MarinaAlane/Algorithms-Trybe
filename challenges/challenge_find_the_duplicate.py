def find_duplicate(nums):
    if nums == '' or len(nums) == 0 or isinstance(nums,str):
        return False
    else:
        found = set()
        for num in nums:
            if num in found and num > 0:
                return num
            found.add(num)
        return False
