def study_schedule(permanence_period, target_time):
    amount = 0

    if not target_time:
        return None
    for start_time, final_time in permanence_period:
        if type(start_time) is not int or type(final_time) is not int:
            return None
        if start_time <= target_time <= final_time:
            amount += 1

    return amount
