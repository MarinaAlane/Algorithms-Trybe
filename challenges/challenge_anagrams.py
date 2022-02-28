def insertion_sort(word):
    word_list = list(word)

    for i in range(len(word_list)):
        current_value = word_list[i]
        current_position = i
        while (
            current_position > 0 and word_list[current_position -
                                               1] > current_value
        ):
            word_list[current_position] = word_list[current_position - 1]
            current_position = current_position - 1
        word_list[current_position] = current_value
    return word_list


def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False
    if insertion_sort(first_string) == insertion_sort(second_string):
        return True
    else:
        return False
