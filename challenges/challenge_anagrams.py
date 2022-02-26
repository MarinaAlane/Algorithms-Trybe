def string_to_sorted_list(str):
    list_base = list(str)
    list_to_return = list()

    for item in range(len(list_base)):
        min_str = min(list_base)
        list_to_return.append(min_str)
        list_base.remove(min_str)

    return list_to_return


def is_anagram(first_string, second_string):
    result = string_to_sorted_list(first_string) == string_to_sorted_list(
        second_string
    )
    return result
