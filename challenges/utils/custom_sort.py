def custom_sort(string):
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
    return custom_sort(left) + middle + custom_sort(right)
