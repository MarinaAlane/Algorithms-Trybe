from tokenize import Number


def study_schedule(permanence_period, target_time):
    if(target_time is None):
        return None
    sum = 0
    for period1, period2 in permanence_period:
        if(period1 is not Number or period2 is not Number):
            return None
        if(period1 <= target_time <= period2):
            sum += 1
    return sum
