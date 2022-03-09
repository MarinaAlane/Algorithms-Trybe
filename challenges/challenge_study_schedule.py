def study_schedule(permanence_period, target_time):
    students_in_period = 0
    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                students_in_period += 1
        return students_in_period
    except TypeError:
        return None
