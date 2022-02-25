# def sort(array):
#     for i in range(len(array)):
#         first = i
#         for j in range(i + 1, len(array)):
#             if (array[j] < array[first]):
#                 first = j
#         array[first], array[i] = array[i], array[first]
#     return array

def is_anagram(first_string, second_string):
    first = list(first_string)
    second = list(second_string)
    quickSort(first, 0, len(first) - 1)
    quickSort(second, 0, len(second) - 1)
    # print(first)
    # print(second)
    try:
        if len(first_string) != len(second_string):
            return False
        # list_exist = []
        # for i in first_string:
        #     includ = second_string.find(i)
        #     if includ != -1:
        #         list_exist.append(i)
        if (first == second):
            return True
    except TypeError:
        return False
    return False
    """ Faça o código aqui. """
# https://www.afternerd.com/blog/python-string-contains/
# https://stackoverflow.com/questions/113655/is-there-a-function-in-python-to-split-a-word-into-a-list

def partition(tempList, low, high):
    i = low - 1
    pivot = tempList[high]
    for j in range(low, high):
        if tempList[j] <= pivot:
            i += 1
            tempList[i], tempList[j] = tempList[j], tempList[i]
    tempList[i+1], tempList[high] = tempList[high], tempList[i+1]
    return (i+1)


def quickSort(tempList, low, high):
    if low < high:
        pi = partition(tempList, low, high)
        quickSort(tempList, low, pi-1)
        quickSort(tempList, pi+1, high)

# unsortedList = [4, 2, 10, 8, 6]
# quickSort(unsortedList, 0, 4)

# https://pythonwife.com/sorting-algorithms-in-python/