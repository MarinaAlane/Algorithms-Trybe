def study_schedule(permanence_period, target_time):
    if type(target_time) is not int:
        return None

    counter = 0

    for start, end in permanence_period:
        if type(start) is not int or type(end) is not int:
            return None

        if start <= target_time <= end:
            counter += 1

    return counter