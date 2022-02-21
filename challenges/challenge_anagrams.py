def new_sort(string):
    if len(string) <= 1:
        return string
    base_letter = string[len(string) // 2]
    middle = []
    left = []
    right = []
    for letter in string:
        if letter > base_letter:
            right.append(letter)
        elif letter < base_letter:
            left.append(letter)
        else:
            middle.append(letter)
    return new_sort(left) + middle + new_sort(right)


def is_anagram(first_string, second_string):
    if len(first_string) is not len(second_string):
        return False
    first_string = "".join(new_sort(first_string))
    second_string = "".join(new_sort(second_string))
    return first_string == second_string
