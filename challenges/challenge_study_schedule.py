def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    counter = 0
    for first_time, last_time in permanence_period:
        if type(first_time) is not int or type(last_time) is not int:
            return None
        if first_time <= target_time <= last_time:
            counter += 1
    return counter
