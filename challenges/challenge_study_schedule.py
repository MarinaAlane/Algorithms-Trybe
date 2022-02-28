def study_schedule(permanence_period, target_time):
    counter = 0
    if not target_time:
        return None
    for period in permanence_period:
        if type(period[0]) is not int or type(period[1]) is not int:
            return None
        if target_time >= period[0] and target_time <= period[1]:
            counter += 1
    return counter
