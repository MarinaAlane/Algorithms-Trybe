def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first_string_list = list(first_string)
    second_string_list = list(second_string)

    for i in range(len(first_string)):
        if first_string_list[i] in second_string_list:
            second_string_list.remove(first_string_list[i])
        else:
            return False

    return True
