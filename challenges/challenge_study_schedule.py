def study_schedule(permanence_period, target_time):
    if(target_time is None):
        return None
    sum = 0
    for period1, period2 in permanence_period:
        if not isinstance(period1, int) or not isinstance(period2, int):
            return None
        if(period1 <= target_time <= period2):
            sum += 1
    return sum
