from challenges import sorting_algs


def find_duplicate(nums):
    if not len(nums) or len(nums) == 1:
        return False

    sorting_algs.quicksort(nums, 0, len(nums) - 1)

    for i, n in enumerate(nums):
        if type(n) == str or n < 0 or i == len(nums) - 1:
            return False
        if n == nums[i + 1]:
            return n
