def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    counter = 0

    for period in permanence_period:
        if type(period[0]) is not int or type(period[1]) is not int:
            return None

        if period[0] <= target_time and period[1] >= target_time:
            counter += 1

    return counter
