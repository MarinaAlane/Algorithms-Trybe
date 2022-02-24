def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    amount = 0
    for first, last in permanence_period:
        if (type(first) is not int or type(last) is not int):
            return None
        if first <= target_time <= last:
            amount += 1
    return amount
