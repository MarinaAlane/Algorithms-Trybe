def study_schedule(permanence_period, target_time):
    students = 0
    for period in permanence_period:
        try:
            if period[0] <= target_time <= period[1]:
                students += 1
        except TypeError:
            return None
    return students
