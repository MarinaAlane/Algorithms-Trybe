def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left, rigth = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, rigth, array.copy())


def merge(left, rigth, merged):
    left_cursor, rigth_cursor = 0, 0
    while left_cursor < len(left) and rigth_cursor < len(rigth):
        if left[left_cursor] <= rigth[rigth_cursor]:
            merged[left_cursor + rigth_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + rigth_cursor] = rigth[rigth_cursor]
            rigth_cursor += 1
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + rigth_cursor] = left[left_cursor]
    for rigth_cursor in range(rigth_cursor, len(rigth)):
        merged[left_cursor + rigth_cursor] = rigth[rigth_cursor]
    return merged


def find_duplicate(nums):
    if len(nums) <= 1 or type(nums) == str:
        return False
    nums_sorted = merge_sort(nums)
    present_item = nums_sorted[0]
    for num in nums_sorted[1:]:
        if not type(num) == int or num < 0:
            return False
        if num == present_item:
            return num
        present_item = num
    return False
