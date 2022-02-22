# ..Source: https://www.geeksforgeeks.org/python-check-if-a-variable-is-string

def validations(numbers):
    for number in numbers:
        if isinstance(number, str):
            return False
        elif number < 1:
            return False
    return True


def custom_numbers_sort(numbers):
    if validations(numbers) is False:
        return False
    if len(numbers) <= 1:
        return numbers

    base_number = numbers[len(numbers) // 2]

    middle = [number for number in numbers if number == base_number]
    left = [number for number in numbers if number < base_number]
    right = [number for number in numbers if number > base_number]

    return custom_numbers_sort(left) + middle + custom_numbers_sort(right)
