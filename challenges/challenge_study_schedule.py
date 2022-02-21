def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    counter = 0

    for begin, end in permanence_period:
        if type(begin) is not int or type(end) is not int:
            return None

        if begin <= target_time <= end:
            counter += 1

    return counter
