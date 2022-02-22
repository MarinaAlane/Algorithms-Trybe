def custom_numbers_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    base_number = numbers[len(numbers) // 2]
    middle = []
    left = []
    right = []
    for number in numbers:
        if isinstance(number, str):
            return False
        if number < 1:
            return False
        if number > base_number:
            right.append(number)
        elif number < base_number:
            left.append(number)
        else:
            middle.append(number)
    return custom_numbers_sort(left) + middle + custom_numbers_sort(right)
