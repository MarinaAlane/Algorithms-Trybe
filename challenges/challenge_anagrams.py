def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False

    first = sort(list(first_string))
    second = sort(list(second_string))

    if first == second:
        return True
    return False


def sort(word):
    # Peguei uma ajuda do course rsrs
    if len(word) <= 1:
        return word

    mid = len(word) // 2

    left = sort(word[:mid])
    right = sort(word[mid:])

    return merge(left, right, word.copy())


def merge(left, right, merged):

    left_pst = 0
    right_pst = 0

    while left_pst < len(left) and right_pst < len(right):
        if left[left_pst] <= right[right_pst]:
            merged[left_pst + right_pst] = left[left_pst]
            left_pst += 1
        else:
            merged[left_pst + right_pst] = right[right_pst]
            right_pst += 1

    for left_pst in range(left_pst, len(left)):
        merged[left_pst + right_pst] = left[left_pst]

    for right_pst in range(right_pst, len(right)):
        merged[left_pst + right_pst] = right[right_pst]

    return merged