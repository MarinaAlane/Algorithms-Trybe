def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    if len(first_string) != len(second_string):
        return False
    return bubble_sort(first_string) == bubble_sort(second_string)


def bubble_sort(string):
    str_list = list(string)
    has_swapped = True
    print(str_list)

    num_of_iterations = 0

    while has_swapped:
        has_swapped = False
        for i in range(len(str_list) - num_of_iterations - 1):
            if str_list[i] > str_list[i + 1]:
                str_list[i], str_list[i + 1] = str_list[i + 1], str_list[i]
                has_swapped = True
        num_of_iterations += 1
    return "".join(str_list)
