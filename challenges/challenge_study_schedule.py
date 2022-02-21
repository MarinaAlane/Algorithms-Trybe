def study_schedule(permanence_period, target_time):
    result = 0

    if not bool(target_time):
        return None

    for number in permanence_period:
        if not isinstance(number[0], int) or not isinstance(number[1], int):
            return None
        if number[0] <= target_time <= number[1]:
            result += 1
    return result


permanence_period = [(2, 2), (1, 2), ("a", 3), (1, 5), (4, 5), (4, 5)]
