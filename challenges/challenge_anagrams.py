def my_sort(string):
    array = list(string)
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return "".join(array)


def is_anagram(first_string, second_string):
    first_sorted = my_sort(first_string)
    second_sorted = my_sort(second_string)
    return first_sorted == second_sorted
