def contains_duplicate(numbers, target_time):
    if not target_time:
        return None

    counter = 0

    for number in numbers:
        if type(number[0]) != int or type(number[1]) != int:
            return None

        if number[0] <= target_time and number[1] >= target_time:
            counter += 1

    return counter


def study_schedule(permanence_period, target_time):
    return contains_duplicate(permanence_period, target_time)
