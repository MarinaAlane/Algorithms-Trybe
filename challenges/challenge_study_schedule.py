def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    counter = 0

    for number in permanence_period:
        if type(number[0]) != int or type(number[1]) != int:
            return None
        if number[0] <= target_time and number[1] >= target_time:
            counter += 1

    return counter
