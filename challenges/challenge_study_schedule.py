def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    count = 0
    for start, end in permanence_period:
        if type(start) is not int or type(end) is not int:
            return None

        if start <= target_time <= end:
            count += 1

    return count
