def insertion_sort(string_list):
    for i in range(len(string_list)):
        current_value = string_list[i]
        current_position = i
        while (
            current_position > 0
            and string_list[current_position - 1] > current_value
        ):
            string_list[current_position] = string_list[current_position - 1]
            current_position = current_position - 1
        string_list[current_position] = current_value
    return string_list


def is_anagram(first_string, second_string):
    ordened_first_string_list = insertion_sort(list(first_string))
    ordened_second_string_list = insertion_sort(list(second_string))
    if ordened_first_string_list == ordened_second_string_list:
        return True
    else:
        return False


# print(is_anagram("Lorem ipsum dolor sit amet, consectetur "
#                  "adipiscing elit, do sed eiusmod tempor "
#                  "incididunt ut labore et dolore magna aliqua.",
#                  "Lorem ipsum dolor sit amet, consectetur "
#                  "adipiscing elit, do sed eiusmod tempor "
#                  "incididunt ut labore et dolore magna aliqua."))
