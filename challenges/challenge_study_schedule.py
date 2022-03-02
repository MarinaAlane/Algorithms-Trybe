def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    students_per_period = 0
    for period in permanence_period:
        if target_time >= period[0] and target_time <= period[1]:
            students_per_period += 1
    return students_per_period
