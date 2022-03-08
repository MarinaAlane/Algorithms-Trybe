def study_schedule(permanence_period, target_time):
    count = 0
    if type(target_time) is not int:
        return None
    for period1, period2 in permanence_period:
        if (type(period1) is int) and (type(period2) is int):
            if target_time >= period1 and target_time <= period2:
                count += 1
        else:
            return None
    return count
