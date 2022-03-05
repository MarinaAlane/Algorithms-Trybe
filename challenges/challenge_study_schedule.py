def study_schedule(permanence_period, target_time):
    count = 0

    if target_time is None:
        return None

    for period in permanence_period:
        if not isinstance(period[0], int) or not isinstance(period[1], int):
            return None

        if period[0] <= target_time and period[1] >= target_time:
            count += 1

    return count
