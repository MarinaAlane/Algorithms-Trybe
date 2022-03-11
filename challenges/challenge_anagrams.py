def toSort(list):
    base_list = len(list) + 1
    sorted_list = []
    counter = 1
    while counter < base_list:
        minimum = min(list)
        id = list.index(minimum)
        del(list[id])
        sorted_list.append(minimum)
        counter += 1

    return sorted_list


def is_anagram(first_string, second_string):
    if (
        first_string == ""
        or second_string == ""
    ):
        return False
    a = toSort(list(first_string))
    b = toSort(list(second_string))
    if a == b:
        return True
    else:
        return False