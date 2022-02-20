# def find_duplicate(nums):
#     duplicate = False
#     try:
#         nums.sort()
#         index = 0
#         # if nums[index] <= 0:
#         #     raise Exception
#         while not duplicate and index < len(nums) - 1:
#             if nums[index] == nums[index + 1] and nums[index] > 0:
#                 duplicate = nums[index]
#             else:
#                 index += 1
#         return duplicate
#     except Exception:
#         return duplicate

def find_duplicate(nums):
    duplicate = False
    try:
        nums.sort()
        for index, item in enumerate(nums):
            if item == nums[index + 1] and item > 0:
                duplicate = nums[index]
                break
        return duplicate
    except Exception:
        return duplicate
