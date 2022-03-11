# https://www.quora.com/How-do-I-sort-a-string-alphabetically-in-Python-without-using-the-sort-function
def is_anagram(first_string, second_string):
    str1 = sorting_a_string(first_string)
    str2 = sorting_a_string(second_string)
    return str1 == str2


def sorting_a_string(some_string):
    my_new_string = ''
    my_list = [
        element for element in some_string.lower() if ord(element) in range(
                                                                ord('a'),
                                                                ord('z') + 1)
        ]

    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i - 1
        while j >= 0 and key < my_list[j]:
            my_list[j+1] = my_list[j]
            j -= 1
        my_list[j+1] = key

    for element in my_list:
        my_new_string += element

    return my_new_string
