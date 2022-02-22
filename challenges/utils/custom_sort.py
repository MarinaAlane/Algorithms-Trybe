def custom_sort(string):
    if len(string) <= 1:
        return string
    base_letter = string[len(string) // 2]

    middle = [letter for letter in string if letter == base_letter]
    left = [letter for letter in string if letter < base_letter]
    right = [letter for letter in string if letter > base_letter]

    return custom_sort(left) + middle + custom_sort(right)
