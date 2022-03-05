def order_function(string):
    string_arr = list(string)
    new_list = list()

    while string_arr:
        min = string_arr[0]

        for char in string_arr:
            if char <= min:
                min = char
        
        string_arr.remove(min)
        new_list.append(min)

    return new_list


def is_anagram(first_string, second_string):
    first = order_function(first_string)
    second = order_function(second_string)

    return first == second
