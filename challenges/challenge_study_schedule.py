def study_schedule(permanence_period, target_time):
    count_study = 0
    if type(target_time) is not int:
        return None

    for period_study in permanence_period:
        permanence_zero = isinstance(period_study[0], int)
        permanence_one = isinstance(period_study[1], int)
        if not permanence_zero or not permanence_one:
            return None

        if period_study[0] <= target_time <= period_study[1]:
            count_study += 1

    return count_study
