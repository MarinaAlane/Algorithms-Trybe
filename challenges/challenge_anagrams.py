def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    elif order_function(first_string) == order_function(second_string):
        return True
    return False


def order_function(word):
    new_array_list = list()
    word_array_list = list(word)

    while word_array_list:
        min_word = word_array_list[0]
        for letter in word_array_list:
            if letter <= min_word:
                min_word = letter
        new_array_list.append(min_word)
        word_array_list.remove(min_word)
    return new_array_list
