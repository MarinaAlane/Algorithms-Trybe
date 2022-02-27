def my_order_function(word):
    array_word = list(word)
    new_array = []

    while array_word:
        minimum = array_word[0]
        for letter in array_word:
            if letter <= minimum:
                minimum = letter
        new_array.append(minimum)
        array_word.remove(minimum)

    return new_array


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    elif my_order_function(first_string) == my_order_function(second_string):
        return True
    else:
        return False


if __name__ == "__main__":
    # print(is_anagram("pedra", "perda"))
    print(my_order_function("pedra"))
    # print(my_order_function("perda"))
