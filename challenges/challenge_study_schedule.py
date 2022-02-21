def study_schedule(permanence_period, target_time):
    if type(target_time) is not int:
        return None

    counter = 0
    for start_time, end_time in permanence_period:
        if (
            type(start_time) is not int
            or type(end_time) is not int
        ):
            counter = None
            break

        if start_time <= target_time <= end_time:
            counter += 1

    return counter
