def find_duplicate(nums):
    if not isinstance(nums, list):
        return False

    rep_list = []

    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False
        if nums.count(num) > 1:
            rep_list.append(num)

    return rep_list[0] if len(set(rep_list)) == 1 else False
