from tokenize import Number


def study_schedule(permanence_period, target_time):
    if(target_time is None):
        return target_time

    sum = 0
    for period in permanence_period:
        if(period[0] is not Number or period[1] is not Number):
            return None
        if(period[0] <= target_time <= period[1]):
            sum = sum + 1
    return sum
