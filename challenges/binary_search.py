def binary_search(list, target):
    mid = len(list) // 2

    if list[mid] == target:
        return True

    if len(list) == 1:
        return False

    if list[mid] < target:
        return binary_search(list[mid:], target)

    return binary_search(list[:mid], target)
